#include <cstdio>
#include <cassert>
#include <map>

#define noPRINT_INPUT
#define noDEBUG
#define noDEBUG_TERMINATE

#define MIN_KEYTYPE	1
#define MAX_KEYTYPE	200
//#define MAX_CHEST	200
#define MAX_CHEST	20

class Chest {
public:
	Chest(int key, int keys)
	{
		mKey = key;
		mNumOfKeysIn = keys;
		mIsOpen = false;
		for (int i=0; i<MAX_KEYTYPE; ++i)
		{
			mKeysIn[i] = 0;
		}
	}

	void addKey(int keyType)
	{
		assert((keyType >= 1) && (keyType <= 200));
		++mKeysIn[keyType-1];
	}

	int getKey() { return mKey; }
	int getNumOfKeysIn() { return mNumOfKeysIn; }
	int getKeysIn(int keyType)
	{
		assert((keyType >= MIN_KEYTYPE) && (keyType <= MAX_KEYTYPE));
		return mKeysIn[keyType-1];
	}

	bool isOpen() { return mIsOpen; }
	void setOpen(bool open) { mIsOpen = open; }

private:
	int mKey;
	int mNumOfKeysIn;
	int mKeysIn[MAX_KEYTYPE];
	bool mIsOpen;

	int mNumOfValidKeysIn;
};

class Case {
public:
	Case(int K, int N)
	{
		mK = K;
		mN = N;
		for (int i=0; i<MAX_KEYTYPE; ++i)
		{
			mKeys[i] = 0;
		}
		for (int i=0; i<MAX_CHEST; ++i)
		{
			mChests[i] = NULL;
			mChestStack[i] = 0;
		}
		mChestIdx = 0;
		mChestStackIdx = 0;

	}
	virtual ~Case()
	{
	}

#if 0	
	// copy ctor
	Case(Case& rhs)
	{
		assert(rhs.mChestIdx == rhs.mN);
		mK = rhs.mK;
		mN = rhs.mN;
		mChestIdx = rhs.mChestIdx;

		for (int i=0; i<MAX_KEYTYPE; ++i)
		{
			mKeys[i] = rhs.mKeys[i];
		}
		for (int i=0; i<mN; ++i)
		{
			mChests[i] = rhs.mChests[i];
			mChests[i]->setOpen(false); // close back
		}
	}
#endif
	
	void addKey(int keyType, int numOfKeys)
	{
		assert((keyType >= MIN_KEYTYPE) && (keyType <= MAX_KEYTYPE));
		mKeys[keyType-1] += numOfKeys;
	}

	void addChest(Chest* chest)
	{
		mChests[mChestIdx++] = chest;
	}

	int getN() { return mN; }


	bool checkKeyNumbersForClosedChests()
	{
		bool result = true;

		int keysNeeded[MAX_KEYTYPE];
		int keysPresent[MAX_KEYTYPE];
		for (int i=0; i<MAX_KEYTYPE; ++i)
		{
			keysNeeded[i] = 0;
			keysPresent[i] = mKeys[i];
		}

		for (int i=0; i<mN; ++i)
		{
			if (!mChests[i]->isOpen())
			{
				keysNeeded[mChests[i]->getKey()-1]++;

				for (int j=0; j<MAX_KEYTYPE; ++j)
				{
					if (mChests[i]->getKeysIn(j+1) > 0)
					{
						keysPresent[j] += mChests[i]->getKeysIn(j+1);
					}
				}
			}
		}

		for (int i=0; i<MAX_KEYTYPE; ++i)
		{
			if (keysNeeded[i] > keysPresent[i])
			{
#ifdef DEBUG_TERMINATE
				printf("key %d is needed %d but only %d\n", i+1, keysNeeded[i], keysPresent[i]);
#endif
				result = false;
				break;
			}
			else if ((keysNeeded[i] == 1) && (keysPresent[i] == 1))
			{
				for (int n=0; n<mN; ++n)
				{
					if ((!mChests[n]->isOpen()) && (mChests[n]->getKey() == (i+1)) && (mChests[n]->getKeysIn(i+1) == 1))
					{
#ifdef DEBUG_TERMINATE
						printf("key %d is locked at chest %d.\n");
#endif
						result = false;
						break;
					}
				}
			}
		}

		return result;
	}
#if 0
	bool result()
	{
		int openCount = 0;

		for (int i=0; i<MAX_KEYTYPE; ++i)
		{
			if (mKeys[i] > 0)
			{
#ifdef DEBUG
				printf("mKeys[%d]:%d\n", i, mKeys[i]);
#endif
				for (int n=0; n<mN; ++n)
				{
					if ((!mChests[n]->isOpen()) && ((mChests[n]->getKey()-1) == i))
					{
						mChests[n]->setOpen(true);
						mKeys[i]--;
						getKeysFromChest(mChests[n]);
						i = 0;
						++openCount;
#ifdef DEBUG
						printf("OC:%d chest:%d\n", openCount, n);
#endif
						if (openCount >= mN)
						{
							return true;
						}
						continue;
					}
				}
			}
		}

		return false;
	}
#endif

	bool open(int idx)
	{
		assert(mChests[idx]->isOpen() == false);

		bool result = false;
		int chestKeyType = mChests[idx]->getKey();
		if (hasKeyLeft(chestKeyType))
		{
			if (!checkKeyNumbersForClosedChests())
			{
				return false;
			}

#ifdef DEBUG_TERMINATE
			printf("opening %d\n", idx);
#endif
			pushIdx(idx);
			useKey(chestKeyType);
			mChests[idx]->setOpen(true);
			getKeysFromChest(mChests[idx]);

			int openCount = 0;
			for (int i=0; i<mN; ++i)
			{
				if (!mChests[i]->isOpen())
				{
					if (open(i))
					{
						result = true;
						break;
					}
					else
					{
#ifdef DEBUG_TERMINATE
						printf("open failed at %d\n", i);
#endif
					}
				}
				else
				{
					++openCount;
				}
			}
			
			if (openCount == mN)
			{
				result = true;
			}

			if (result == false)
			{
#ifdef DEBUG_TERMINATE
				printf("closing %d\n", idx);
#endif
				// close me back
				giveKeysToChest(mChests[idx]);
				mChests[idx]->setOpen(false);
				unuseKey(chestKeyType);
				popIdx(idx);
			}
		}
		else
		{
			result = false;
		}

		return result;
	}

	void printChestStack()
	{
		for (int i=0; i<mChestStackIdx; ++i)
		{
			printf(" %d", (mChestStack[i] + 1));
		}
	}

private:
	bool hasKeyLeft(int keyType)
	{
		assert((keyType >= MIN_KEYTYPE) && (keyType <= MAX_KEYTYPE));
#ifdef DEBUG
		printf("hasKeyLeft:%d %d\n", keyType, mKeys[keyType-1]);
#endif
		return (mKeys[keyType-1] > 0) ? true : false;
	}
	void useKey(int keyType)
	{
		assert(mKeys[keyType-1] > 0);
		--mKeys[keyType-1];
	}
	void unuseKey(int keyType)
	{
		++mKeys[keyType-1];
	}

	void getKeysFromChest(Chest* chest)
	{
		int num = chest->getNumOfKeysIn();
		int keyType = 1;
		while (num > 0)
		{
			int keysFromChest = chest->getKeysIn(keyType);
			if (keysFromChest > 0)
			{
#ifdef DEBUG_TERMINATE
				printf("getKeysFromChest keyType:%d num:%d, keysFromChest:%d\n", keyType, num, keysFromChest);
#endif
				addKey(keyType, keysFromChest);
				num -= keysFromChest;
			}
			++keyType;
			assert(keyType <= MAX_KEYTYPE);
		}
	}

	void giveKeysToChest(Chest* chest)
	{
		int num = chest->getNumOfKeysIn();
		int keyType = 1;
		while (num > 0)
		{
			int keysFromChest = chest->getKeysIn(keyType);
			if (keysFromChest > 0)
			{
				addKey(keyType, (-1) * keysFromChest);
				num -= keysFromChest;
			}
			++keyType;
			assert(keyType <= MAX_KEYTYPE);
		}
	}

	void pushIdx(int idx)
	{
#ifdef DEBUG
		printf("  push - mChestStackIdx:%d %d\n", mChestStackIdx, idx);
#endif
		mChestStack[mChestStackIdx++] = idx;
	}

	void popIdx(int idx)
	{
		assert(mChestStack[--mChestStackIdx] == idx);
#ifdef DEBUG
		printf("  pop - mChestStackIdx:%d %d\n", mChestStackIdx, mChestStack[mChestStackIdx]);
#endif
		mChestStack[mChestStackIdx] = 0;
	}

private:
	int mK;
	int mN;
	int mKeys[MAX_KEYTYPE];
	Chest* mChests[MAX_CHEST];
	int mChestIdx;

	int mChestStack[MAX_CHEST];
	int mChestStackIdx;
};

int main(int argc, char** argv)
{
	FILE* in = fopen(argv[1], "r");
	assert(in != NULL);

	int T = 0;
	fscanf(in, "%d\n", &T);
#ifdef PRINT_INPUT
	printf("T:%d\n", T);
#endif

	for (int t=0; t<T; ++t)
	{
		int K, N;
		fscanf(in, "%d %d\n", &K, &N);
#ifdef PRINT_INPUT
		printf("K:%d N:%d\n", K, N);
#endif
		Case c(K, N);
		int keyType;
		for (int k=0; k<K; ++k)
		{
			fscanf(in, "%d ", &keyType);
#ifdef PRINT_INPUT
			printf("addKey:%d\n", keyType);
#endif
			c.addKey(keyType, 1);
		}

		int chestKey, keys;
		Chest* chest[MAX_CHEST];
		for (int n=0; n<N; ++n)
		{
			fscanf(in, "%d %d ", &chestKey, &keys);
#ifdef PRINT_INPUT
			printf("chest:%d key:%d hasKey:%d\n", n, chestKey, keys);
#endif
			chest[n] = new Chest(chestKey, keys);
			for (int k=0; k<keys; ++k)
			{
				fscanf(in, "%d ", &keyType);
#ifdef PRINT_INPUT
				printf("addKey:%d\n", keyType);
#endif
				chest[n]->addKey(keyType);
			}

			c.addChest(chest[n]);
		}


		// loop iteration starting each chest
		bool isPossible = false;

		//isPossible = c.checkKeyNumbers();
		//if (isPossible)
		{
			for (int i=0; i<c.getN(); ++i)
			{
				//printf("###### %d ######\n", i);
				if (c.open(i))
				{
					printf("Case #%d:", (t+1));
					c.printChestStack();
					printf("\n");
					isPossible = true;
					break;
				}
			}
			//isPossible = c.result();
		}

		if (!isPossible)
		{
			printf("Case #%d: IMPOSSIBLE\n", (t+1));
		}

		// tear down
		for (int n=0; n<N; ++n)
		{
			delete chest[n];
		}
	} // for (int t=0; t<T; ++t)

	fclose(in);
}

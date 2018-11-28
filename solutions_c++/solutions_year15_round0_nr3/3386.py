#include <fstream>

using namespace std;

const char InFile[] = "input.in";
const char OutFile[] = "output.out";
const int MaxN = 10111;

ifstream fin(InFile);
ofstream fout(OutFile);

int T, L, X;
char str[MaxN];

struct Quat4
{
	Quat4(int x=0, int y=0, int z=0, int w=0) :x(x),y(y),z(z),w(w){}
	int x, y, z, w;

	inline bool operator== (const Quat4 &other) const
	{
		return other.x == x && other.y == y && other.z == z && other.w == w;
	}
};

Quat4 mul(Quat4 q1, Quat4 q2) {
	int x = q1.x * q2.w + q1.y * q2.z - q1.z * q2.y + q1.w * q2.x;
	int y = -q1.x * q2.z + q1.y * q2.w + q1.z * q2.x + q1.w * q2.y;
	int z = q1.x * q2.y - q1.y * q2.x + q1.z * q2.w + q1.w * q2.z;
	int w = -q1.x * q2.x - q1.y * q2.y - q1.z * q2.z + q1.w * q2.w;
	return Quat4(x,y,z,w);
}

Quat4 getQ(char ch)
{
	if (ch == 'i')
	{
		return Quat4(1,0,0,0);
	}
	if (ch == 'j')
	{
		return Quat4(0,1,0,0);
	}
	if (ch == 'k')
	{
		return Quat4(0,0,1,0);
	}
	return Quat4(0,0,0,1);
}

int main()
{
	fin >> T;
	for (int test = 1; test <= T; ++test)
	{
		bool ok = false;

		fin >> L >> X;
		fin >> str;

		for (int i = L; i < L*X; ++i)
		{
			str[i] = str[i-L];
		}
		str[L*X] = 0;

		Quat4 leftVal = getQ(1);
		int left=0;
		while (left < L*X)
		{
			leftVal = mul(leftVal,getQ(str[left]));
			++left;
			if (leftVal == getQ('i'))
			{
				break;
			}
		}

		Quat4 rightVal = getQ(1);
		int right = L*X - 1;
		while (right >= 0)
		{
			rightVal = mul(getQ(str[right]),rightVal);
			--right;
			if (rightVal == getQ('k'))
			{
				break;
			}
		}

		if (left <= right)
		{
			Quat4 midVal = getQ(1);
			for (int i = left; i <= right; ++i)
			{
				midVal = mul(midVal, getQ(str[i]));
			}
			if (midVal == getQ('j'))
			{
				ok = true;
			}
		}

		fout << "Case #" << test << ": ";
		if (ok)
		{
			fout << "YES\n";
		}
		else
		{
			fout << "NO\n";
		}
	}
	fin.close();
	fout.close();
	return 0;
}

#pragma once

struct trip
{
	Int n[3];
};
bool operator<(trip t1, trip t2)
{
	if (t1.n[0] < t2.n[0])
		return true;
	if (t1.n[0] > t2.n[0])
		return false;
	if (t1.n[2] < t2.n[2])
		return true;
	if (t1.n[2] > t2.n[2])
		return false;
	if (t1.n[1] < t2.n[1])
		return true;
	if (t1.n[1] > t2.n[1])
		return false;
	return false;
}

template<>
struct CTXData<ProblemB>
{
	Int L;
	Int C[20];
	Int J[20];
	Str CC, JJ;

	Int cC, cJ;

	Int TestOption(Int i, Int & bC, Int &bJ)
	{
		if (i == L)
		{
			return abs(bC - bJ);
		}
		if (C[i] == -1)
		{
			if (J[i] == -1)
			{
				set<trip> trips;
				trip t;
				t.n[1] = bJ;
				t.n[2] = bC;
				t.n[0] = TestOption(i + 1, t.n[2], t.n[1]);
				trips.insert(t);


				t.n[1] = bJ + pow(10, L - i - 1);
				t.n[2] = bC;
				t.n[0] = TestOption(i + 1, t.n[2], t.n[1]);
				trips.insert(t);

				t.n[1] = bJ;
				t.n[2] = bC + pow(10, L - i - 1) * 9;
				t.n[0] = TestOption(i + 1, t.n[2], t.n[1]);
				trips.insert(t);

				t.n[1] = bJ + pow(10, L - i - 1) * 9;
				t.n[2] = bC;
				t.n[0] = TestOption(i + 1, t.n[2], t.n[1]);
				trips.insert(t);

				t.n[1] = bJ;
				t.n[2] = bC + pow(10, L - i - 1);
				t.n[0] = TestOption(i + 1, t.n[2], t.n[1]);
				trips.insert(t);

				trip bT = *trips.begin();
				bC = bT.n[2];
				bJ = bT.n[1];
				return bT.n[0];
			}
			else
			{
				bJ += pow(10, L - i - 1) * J[i];

				set<trip> trips;
				trip t;
				t.n[1] = bJ;
				t.n[2] = bC + pow(10, L - i - 1) * J[i];
				t.n[0] = TestOption(i + 1, t.n[2], t.n[1]);

				trips.insert(t);
				if (J[i] < 9)
				{
					t.n[1] = bJ;
					t.n[2] = bC + pow(10, L - i - 1) * (J[i]+1);
					t.n[0] = TestOption(i + 1, t.n[2], t.n[1]);
					trips.insert(t);
				}

				t.n[1] = bJ;
				t.n[2] = bC;
				t.n[0] = TestOption(i + 1, t.n[2], t.n[1]);
				trips.insert(t);

				if (J[i] > 0)
				{
					t.n[1] = bJ;
					t.n[2] = bC + pow(10, L - i - 1) * (J[i] - 1);
					t.n[0] = TestOption(i + 1, t.n[2], t.n[1]);
					trips.insert(t);
				}

				t.n[1] = bJ;
				t.n[2] = bC + pow(10, L - i - 1) * 9;
				t.n[0] = TestOption(i + 1, t.n[2], t.n[1]);
				trips.insert(t);

				trip bT = *trips.begin();
				bC = bT.n[2];
				bJ = bT.n[1];
				return bT.n[0];
			}

		}
		else
		{
			bC += pow(10, L - i - 1) * C[i];
			if (J[i] != -1)
			{
				bJ += pow(10, L - i - 1) * J[i];
				return TestOption(i + 1, bC, bJ);
			}

			set<trip> trips;
			trip t;
			t.n[1] = bJ + pow(10, L - i - 1) * C[i];
			t.n[2] = bC;
			t.n[0] = TestOption(i + 1, t.n[2], t.n[1]);

			trips.insert(t);
			if (C[i] < 9)
			{
				t.n[1] = bJ + pow(10, L - i - 1) * (C[i] + 1);
				t.n[2] = bC;
				t.n[0] = TestOption(i + 1, t.n[2], t.n[1]);
				trips.insert(t);
			}

				t.n[1] = bJ;
				t.n[2] = bC;
				t.n[0] = TestOption(i + 1, t.n[2], t.n[1]);
				trips.insert(t);

			if (C[i] > 0)
			{
				t.n[1] = bJ + pow(10, L - i - 1) * (C[i] - 1);
				t.n[2] = bC ;
				t.n[0] = TestOption(i + 1, t.n[2], t.n[1]);
				trips.insert(t);
			}

				t.n[1] = bJ + pow(10, L - i - 1) * 9;
				t.n[2] = bC;
				t.n[0] = TestOption(i + 1, t.n[2], t.n[1]);
				trips.insert(t);


			trip bT = *trips.begin();
			bC = bT.n[2];
			bJ = bT.n[1];
			return bT.n[0];
		}
	}
};

template<>
void CTX<ProblemB>::Read()
{
	CC = ReadStr();
	JJ = ReadStr();
	L = JJ.size();
	for (Int i = 0; i < L; i++)
	{
		C[i] = (CC[i] == '?') ? -1 : (CC[i] - '0');
		J[i] = (JJ[i] == '?') ? -1 : (JJ[i] - '0');
	}
	cC = 0;
	cJ = 0;
}

template<>
void CTX<ProblemB>::Solve()
{
	Int bC = 0;
	Int bJ = 0;
	TestOption(0, bC, bJ);

	char f[40];
	sprintf(f, "%%0%dI64d %%0%dI64d", (int)L, (int)L);
	char res[40];
	sprintf(res, f, bC, bJ);
	Write(res);



}
#include <iostream>
#include <fstream>

using namespace std;
int nontrivial(long long int a);
int compute_two(int x, int w, int v, int u, int t, int s, int r, int q, int p, int o, int n, int m, int l, int k, int j, int i);
int compute_three(int x, int w, int v, int u, int t, int s, int r, int q, int p, int o, int n, int m, int l, int k, int j, int i);
int compute_four(int x, int w, int v, int u, int t, int s, int r, int q, int p, int o, int n, int m, int l, int k, int j, int i);
int compute_five(int x, int w, int v, int u, int t, int s, int r, int q, int p, int o, int n, int m, int l, int k, int j, int i);
int compute_six(int x, int w, int v, int u, int t, int s, int r, int q, int p, int o, int n, int m, int l, int k, int j, int i);
int compute_seven(int x, int w, int v, int u, int t, int s, int r, int q, int p, int o, int n, int m, int l, int k, int j, int i);
int compute_eight(int x, int w, int v, int u, int t, int s, int r, int q, int p, int o, int n, int m, int l, int k, int j, int i);
int compute_nine(int x, int w, int v, int u, int t, int s, int r, int q, int p, int o, int n, int m, int l, int k, int j, int i);
int compute_ten(int x, int w, int v, int u, int t, int s, int r, int q, int p, int o, int n, int m, int l, int k, int j, int i);
int main()
{
	fstream myfile;
	ofstream codejam;
	codejam.open("C-small-attempt0.out");

	myfile.open("C-small-attempt0.in");
	char a[1000];
	myfile.getline(a, 1000);
	int T = atoi(a);

	cout << T << endl;
	codejam << "Case #1:";
	int i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x;
	int count = 0;
	int total = 50;

	for (x = 0; x<2; x++)
	{
		for (w = 0; w<2; w++)
		{
			for (v = 0; v<2; v++)
			{
				for (u = 0; u<2; u++)
				{
					for (t = 0; t<2; t++)
					{
						for (s = 0; s<2; s++)
						{
							for (r = 0; r<2; r++)
							{
								for (q = 0; q<2; q++)
								{
									for (p = 0; p<2; p++)
									{
										for (o = 0; o<2; o++)
										{
											for (n = 0; n<2; n++)
											{
												for (m = 0; m<2; m++)
												{
													for (l = 0; l<2; l++)
													{
														for (k = 0; k<2; k++)
														{
															for (j = 0; j<2; j++)
															{
																for (i = 0; i<2; i++)
																{
																	int two, three, four, five, six, seven, eight, nine, ten;
																	if (i == 1 && x == 1)
																	{
																		two = compute_two(x, w, v, u, t, s, r, q, p, o, n, m, l, k, j, i);
																		three = compute_three(x, w, v, u, t, s, r, q, p, o, n, m, l, k, j, i);
																		four = compute_four(x, w, v, u, t, s, r, q, p, o, n, m, l, k, j, i);
																		five = compute_five(x, w, v, u, t, s, r, q, p, o, n, m, l, k, j, i);
																		six = compute_six(x, w, v, u, t, s, r, q, p, o, n, m, l, k, j, i);
																		seven = compute_seven(x, w, v, u, t, s, r, q, p, o, n, m, l, k, j, i);
																		eight = compute_eight(x, w, v, u, t, s, r, q, p, o, n, m, l, k, j, i);
																		nine = compute_nine(x, w, v, u, t, s, r, q, p, o, n, m, l, k, j, i);
																		ten = compute_ten(x, w, v, u, t, s, r, q, p, o, n, m, l, k, j, i);

																		if (two != -1 && three != -1 && four != -1 && five != -1 && six != -1 && seven != -1 && eight != -1 && nine != -1 && ten != -1)
																		{
																			//is a jam coin
																			codejam << endl << x << w << v << u << t << s << r << q << p << o << n << m << l << k << j << i << " " << two << " " << three << " " << four << " " << five << " " << six << " " << seven << " " << eight;
																			codejam << " " << nine << " " << ten;
																			count++;
																			if (count == total)
																			{
																				myfile.close();
																				codejam.close();
																				return 0;
																			}

																		}

																	}


																}


															}
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}

}


int nontrivial(long long int a)
{
	long long int answer = 2;
	int c = sqrt(a) + 1;
	while (answer < c)
	{

		if (a%answer == 0)
		{
			return answer;
		}
		answer++;
	}
	return -1;
}
int compute_two(int x, int w, int v, int u, int t, int s, int r, int q, int p, int o, int n, int m, int l, int k, int j, int i)
{
	double base = 2.0;
	int arr[16] = { i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x };
	double index = 0.0;
	int ind = 0;
	long long int check = 0;
	while (ind != 16)
	{
		if (arr[ind] != 0)
		{
			check = check + pow(base, index);
		}
		ind++;
		index++;
	}
	//number creates in base ten. now lets find the non trival divisor
	return nontrivial(check);

}
int compute_three(int x, int w, int v, int u, int t, int s, int r, int q, int p, int o, int n, int m, int l, int k, int j, int i)
{
	double base = 3.0;
	int arr[16] = { i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x };
	double index = 0.0;
	int ind = 0;
	long long int check = 0;
	while (ind != 16)
	{
		if (arr[ind] != 0)
		{
			check = check + pow(base, index);
		}
		ind++;
		index++;
	}
	//number creates in base ten. now lets find the non trival divisor
	return nontrivial(check);
}
int compute_four(int x, int w, int v, int u, int t, int s, int r, int q, int p, int o, int n, int m, int l, int k, int j, int i)
{
	double base = 4.0;
	int arr[16] = { i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x };
	double index = 0.0;
	int ind = 0;
	long long int check = 0;
	while (ind != 16)
	{
		if (arr[ind] != 0)
		{
			check = check + pow(base, index);
		}
		ind++;
		index++;
	}
	//number creates in base ten. now lets find the non trival divisor
	return nontrivial(check);
}
int compute_five(int x, int w, int v, int u, int t, int s, int r, int q, int p, int o, int n, int m, int l, int k, int j, int i)
{
	double base = 5.0;
	int arr[16] = { i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x };
	double index = 0.0;
	int ind = 0;
	long long int check = 0;
	while (ind != 16)
	{
		if (arr[ind] != 0)
		{
			check = check + pow(base, index);
		}
		ind++;
		index++;
	}
	//number creates in base ten. now lets find the non trival divisor
	return nontrivial(check);
}
int compute_six(int x, int w, int v, int u, int t, int s, int r, int q, int p, int o, int n, int m, int l, int k, int j, int i)
{
	double base = 6.0;
	int arr[16] = { i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x };
	double index = 0.0;
	int ind = 0;
	long long int check = 0;
	while (ind != 16)
	{
		if (arr[ind] != 0)
		{
			check = check + pow(base, index);
		}
		ind++;
		index++;
	}
	//number creates in base ten. now lets find the non trival divisor
	return nontrivial(check);
}
int compute_seven(int x, int w, int v, int u, int t, int s, int r, int q, int p, int o, int n, int m, int l, int k, int j, int i)
{
	double base = 7.0;
	int arr[16] = { i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x };
	double index = 0.0;
	int ind = 0;
	long long int check = 0;
	while (ind != 16)
	{
		if (arr[ind] != 0)
		{
			check = check + pow(base, index);
		}
		ind++;
		index++;
	}
	//number creates in base ten. now lets find the non trival divisor
	return nontrivial(check);
}
int compute_eight(int x, int w, int v, int u, int t, int s, int r, int q, int p, int o, int n, int m, int l, int k, int j, int i)
{
	double base = 8.0;
	int arr[16] = { i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x };
	double index = 0.0;
	int ind = 0;
	long long int check = 0;
	while (ind != 16)
	{
		if (arr[ind] != 0)
		{
			check = check + pow(base, index);
		}
		ind++;
		index++;
	}
	//number creates in base ten. now lets find the non trival divisor
	return nontrivial(check);
}
int compute_nine(int x, int w, int v, int u, int t, int s, int r, int q, int p, int o, int n, int m, int l, int k, int j, int i)
{
	double base = 9.0;
	int arr[16] = { i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x };
	double index = 0.0;
	int ind = 0;
	long long int check = 0;
	while (ind != 16)
	{
		if (arr[ind] != 0)
		{
			check = check + pow(base, index);
		}
		ind++;
		index++;
	}
	//number creates in base ten. now lets find the non trival divisor
	return nontrivial(check);
}
int compute_ten(int x, int w, int v, int u, int t, int s, int r, int q, int p, int o, int n, int m, int l, int k, int j, int i)
{
	double base = 10.0;
	int arr[16] = { i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x };
	double index = 0.0;
	int ind = 0;
	long long int check = 0;
	while (ind != 16)
	{
		if (arr[ind] != 0)
		{
			check = check + pow(base, index);
		}
		ind++;
		index++;
	}
	//number creates in base ten. now lets find the non trival divisor
	return nontrivial(check);
}

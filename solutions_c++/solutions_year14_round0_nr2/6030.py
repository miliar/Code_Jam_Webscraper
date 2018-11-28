#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <iomanip>

using namespace std;

double time_til_cookies(double cookies, double cookies_per_sec)
{
	return cookies / cookies_per_sec;
}

double calc_req_time(double X, double cookies_per_sec)
{
	return time_til_cookies(X, cookies_per_sec);
}

double calc_req_time_with_farm(double C, double F, double X, double cookies_per_sec)
{
	return time_til_cookies(C, cookies_per_sec) + time_til_cookies(X, cookies_per_sec + F);
}

void solve_case(int case_num)
{
	// Input
	double C, F, X;
	cin >> C >> F >> X;

	// Solve
	double cookies_per_sec = 2.0;
	double time_so_far = 0.0;
	double req_time = calc_req_time(X, cookies_per_sec);
	double req_time_with_farm = calc_req_time_with_farm(C, F, X, cookies_per_sec);

	while (req_time_with_farm < req_time)
	{
		time_so_far += time_til_cookies(C, cookies_per_sec);
		cookies_per_sec += F;
		req_time = calc_req_time(X, cookies_per_sec);
		req_time_with_farm = calc_req_time_with_farm(C, F, X, cookies_per_sec);
	}

	time_so_far += req_time;

	// Output
	cout << "Case #" << case_num << ": " << fixed << setprecision(7) << time_so_far << endl;
}

void main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int num_cases;
	cin >> num_cases;

	for (int i = 0; i < num_cases; i++)
	{
		const int case_num = i + 1;
		solve_case(case_num);
	}
}

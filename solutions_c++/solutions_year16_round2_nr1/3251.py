#include <iostream>
#include <algorithm>
#include <stack>
#include <cmath>
#include <cstring>
#include <bits/stdc++.h>
using namespace std;

double PI = 3.1415926535897932384626433832795;




int arr[10];
map<char, int>mp;
string ans;
void zabbat() {
	for(int dig = 0;dig < 10;dig++) {
		if(arr[dig]) {
			int tmp;
			char ch;
			if(dig == 0) {
				tmp = arr[dig];
				mp['Z'] -= tmp;
				mp['E'] -= tmp;
				mp['R'] -= tmp;
				mp['O'] -= tmp;
				ch = '0';
			} else if(dig == 1) {
				tmp = arr[dig];
				mp['O'] -= tmp;
				mp['N'] -= tmp;
				mp['E'] -= tmp;
				ch = '1';
			} else if(dig == 2) {
				tmp = arr[dig];
				mp['T'] -= tmp;
				mp['W'] -= tmp;
				mp['O'] -= tmp;
				ch = '2';
			} else if(dig == 3) {
				tmp = arr[dig];
				mp['T'] -= tmp;
				mp['H'] -= tmp;
				mp['R'] -= tmp;
				mp['E'] -= tmp;
				mp['E'] -= tmp;
				ch = '3';
			} else if(dig == 4) {
				tmp = arr[dig];
				mp['F'] -= tmp;
				mp['O'] -= tmp;
				mp['U'] -= tmp;
				mp['R'] -= tmp;
				ch = '4';
			} else if(dig == 5) {
				tmp = arr[dig];
				mp['F'] -= tmp;
				mp['I'] -= tmp;
				mp['V'] -= tmp;
				mp['E'] -= tmp;
				ch = '5';
			} else if(dig == 6) {
				tmp = arr[dig];
				mp['S'] -= tmp;
				mp['I'] -= tmp;
				mp['X'] -= tmp;
				ch = '6';
			} else if(dig == 7) {
				tmp = arr[dig];
				mp['S'] -= tmp;
				mp['E'] -= tmp;
				mp['V'] -= tmp;
				mp['E'] -= tmp;
				mp['N'] -= tmp;
				ch = '7';
			} else if(dig == 8) {
				tmp = arr[dig];
				mp['E'] -= tmp;
				mp['I'] -= tmp;
				mp['G'] -= tmp;
				mp['H'] -= tmp;
				mp['T'] -= tmp;
				ch = '8';
			} else {
				tmp = arr[dig];
				mp['N'] -= tmp;
				mp['I'] -= tmp;
				mp['N'] -= tmp;
				mp['E'] -= tmp;
				ch = '9';
			}
			while(tmp--) {
				ans += ch;
			}
		}
	}
}


int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int t, cas = 1;
	cin >> t;
	while(t--) {
		string s;
		cin >> s;
		ans = "";
		memset(arr, 0, sizeof arr);
		mp.clear();
		for(int i = 0;i < s.size();i++) {
			mp[s[i]]++;
			if(s[i] == 'Z')
				arr[0]++;
			else if(s[i] == 'W')
				arr[2]++;
			else if(s[i] == 'U')
				arr[4]++;
			else if(s[i] == 'X')
				arr[6]++;
			else if(s[i] == 'G')
				arr[8]++;
		}
		//zabbat
		zabbat();
//		cout << ans << endl;
		memset(arr, 0, sizeof arr);
		for(auto it : mp) {
//			cout << it.first << ' ' << it.second << endl;
			if(it.second != 0) {
				if(it.first == 'O') {
					arr[1] = it.second;
				} else if(it.first == 'H') {
					arr[3] = it.second;
				} else if(it.first == 'F') {
					arr[5] = it.second;
				} else if(it.first == 'S') {
					arr[7] = it.second;
				}
			}
		}
		//zabbat
		zabbat();
		while(mp['I']--) {
			ans += '9';
		}
		sort(ans.begin(), ans.end());
		printf("Case #%d: %s\n", cas++, ans.c_str());
	}
	return 0;
}

















//
///*
// * w a7la salam le Dr.Reda bta3 el graphics ele 3alemna ne3mel clipping w 3alemna ezay nebarmag xD !!
// * Thank you Dr.Reda :D
// */
//
//
//
//
//
//
//
//
//pair<double, double> VIntersect(pair<double, double> v1,
//		pair<double, double> v2, double x) {
//	pair<double, double> intersect;
//	intersect.first = x;
//	intersect.second = v2.second
//			- (v2.first - x) * (v2.second - v1.second) / (v2.first - v1.first);
//	return intersect;
//}
//
//pair<double, double> HIntersect(pair<double, double> v1,
//		pair<double, double> v2, double y) {
//	pair<double, double> intersect;
//	intersect.second = y;
//	intersect.first = v2.first
//			- (v2.second - y) * (v2.first - v1.first)
//					/ (v2.second - v1.second);
//	return intersect;
//}
//
//vector<pair<double, double> > clipleft(vector<pair<double, double> > p1,
//		double x) {
//	vector<pair<double, double> > ret;
//	int sz = p1.size();
//	bool in1 = p1[sz - 1].first < x ? 0 : 1;
//	pair<double, double> v1 = p1[sz - 1];
//	for (int i = 0; i < sz; i++) {
//		bool in2 = p1[i].first < x ? 0 : 1;
//		pair<double, double> v2 = p1[i];
//		if (!in1 and in2) {
//			ret.push_back(VIntersect(v1, v2, x));
//			ret.push_back(v2);
//		} else if(in1 and in2) {
//			ret.push_back(v2);
//		} else if (in1) {
//			ret.push_back(VIntersect(v1, v2, x));
//		}
//		v1 = v2;
//		in1 = in2;
//	}
//	return ret;
//}
//
//vector<pair<double, double> > clipright(vector<pair<double, double> > p1,
//		double x) {
//	vector<pair<double, double> > ret;
//	int sz = p1.size();
//	bool in1 = p1[sz - 1].first > x ? 0 : 1;
//	pair<double, double> v1 = p1[sz - 1];
//	for (int i = 0; i < sz; i++) {
//			bool in2 = p1[i].first > x ? 0 : 1;
//			pair<double, double> v2 = p1[i];
//			if (!in1 and in2) {
//				ret.push_back(VIntersect(v1, v2, x));
//				ret.push_back(v2);
//			} else if(in1 and in2) {
//				ret.push_back(v2);
//			} else if (in1) {
//				ret.push_back(VIntersect(v1, v2, x));
//			}
//			v1 = v2;
//			in1 = in2;
//		}
//	return ret;
//}
//
//vector<pair<double, double> > cliptop(vector<pair<double, double> > p1,
//		double y) {
//	vector<pair<double, double> > ret;
//	int sz = p1.size();
//	bool in1 = p1[sz - 1].second > y ? 0 : 1;
//	pair<double, double> v1 = p1[sz - 1];
//	for (int i = 0; i < sz; i++) {
//			bool in2 = p1[i].second > y ? 0 : 1;
//			pair<double, double> v2 = p1[i];
//			if (!in1 and in2) {
//				ret.push_back(HIntersect(v1, v2, y));
//				ret.push_back(v2);
//			} else if(in1 and in2) {
//				ret.push_back(v2);
//			} else if (in1) {
//				ret.push_back(HIntersect(v1, v2, y));
//			}
//			v1 = v2;
//			in1 = in2;
//		}
//	return ret;
//}
//
//vector<pair<double, double> > clipbottom(vector<pair<double, double> > p1,
//		double y) {
//	vector<pair<double, double> > ret;
//	int sz = p1.size();
//	bool in1 = p1[sz - 1].second < y ? 0 : 1;
//	pair<double, double> v1 = p1[sz - 1];
//	for (int i = 0; i < sz; i++) {
//			bool in2 = p1[i].second < y ? 0 : 1;
//			pair<double, double> v2 = p1[i];
//			if (!in1 and in2) {
//				ret.push_back(HIntersect(v1, v2, y));
//				ret.push_back(v2);
//			} else if(in1 and in2) {
//				ret.push_back(v2);
//			} else if (in1) {
//				ret.push_back(HIntersect(v1, v2, y));
//			}
//			v1 = v2;
//			in1 = in2;
//		}
//	return ret;
//}
//
//int main() {
//	double w, h, a,a2, a3, a4, aa;
//	cin >> w >> h >> aa;
//	a = aa * PI / 180 + atan2(h, w);
//	a2 = aa * PI / 180 + atan2(h, -w);
//	a3 = aa * PI / 180 + atan2(-h, -w);
//	a4 = aa * PI / 180 + atan2(-h, w);
//	double r = (sqrt(w * w / 4.0 + h * h / 4.0));
//	vector<pair<double, double> > pol1 = { { w / 2, h / 2 }, { -w / 2, h / 2 },
//			{ -w / 2, -h / 2 }, { w / 2, -h / 2 }};
//	vector<pair<double, double> > pol2 = { { r*cos(a), r*sin(a) }, { r*cos(a2), r*sin(a2) },
//			{ r*cos(a3), r*sin(a3) }, { r*cos(a4), r*sin(a4) } };
//	pol2 = clipleft(pol2, -w / 2.0);
//	pol2 = cliptop(pol2, h / 2.0);
//	pol2 = clipright(pol2, w / 2.0);
//	pol2 = clipbottom(pol2, -h / 2.0);
//	double area = 0.0;
//	int prev = pol2.size() - 1;
//	for (int i = 0; i < pol2.size(); i++) {
//		area += pol2[prev].first * pol2[i].second
//				- pol2[prev].second * pol2[i].first;
//		prev = i;
//	}
//	cout << fixed << setprecision(10) << area / 2.0 << endl;
//	return 0;
//}

/*input
100
2 3 2
1 1 1
2 1 2
3 2 3
90 5 90
64 4 64
2 59 2
87 8 87
70 7 70
57 9 57
35 2 35
100 4 100
36 11 36
12 4 12
22 12 22
1 2 1
34 10 34
2 18 2
1 100 1
7 16 7
39 9 39
4 4 4
3 37 3
40 8 40
51 9 51
23 8 23
75 3 75
16 11 16
12 8 12
84 3 84
10 5 10
60 9 60
100 1 100
3 36 3
19 14 19
49 6 49
80 8 80
12 6 12
47 1 47
98 4 98
19 8 19
100 2 100
5 19 5
69 4 69
3 23 3
18 5 18
2 49 2
68 9 68
1 60 1
2 4 2
14 7 14
1 87 1
51 3 51
1 3 1
1 49 1
72 2 72
3 3 3
2 13 2
32 11 32
75 8 75
1 63 1
1 4 1
46 5 46
85 5 85
13 9 13
2 2 2
35 4 35
100 9 100
52 8 52
2 29 2
1 10 1
47 9 47
15 11 15
1 90 1
42 7 42
2 25 2
3 4 3
62 8 62
19 1 19
40 1 40
6 10 6
81 6 81
4 3 4
55 1 55
5 9 5
36 1 36
4 2 4
10 8 10
92 2 92
35 8 35
100 3 100
1 21 1
4 1 4
22 8 22
52 7 52
82 6 82
36 10 36
3 1 3
10 18 10
4 29 4


*/
#include <bits/stdc++.h>
#include<stdio.h>
#include<math.h>
using namespace std;
#define pii pair<long long,long long>
#define PI 3.14159265
#define ll long long
#define ff first
#define ss second
#define pb push_back
#define INF 1000000009
#define mod 1000000007

int main() 
{
    std::ios::sync_with_stdio(false);
 	ll t;
 	cin>>t;
 	for(ll m=1;m<=t;++m)
 	{
 		ll k,c,s;
 		cin>>k>>c>>s;
 		if(k==1)
 			cout<<"Case #"<<m<<": 1\n";
 		else if(c==1) 
 		{
 			if(s<k)
 				cout<<"Case #"<<m<<": IMPOSSIBLE\n";
 			else
 			{
 				cout<<"Case #"<<m<<": ";
 				for(ll j=1;j<=k;++j)
 				{
 					cout<<j<<" ";
 				}
 				cout<<endl;
 			}
 		}
 		else
 		{
 			if(s<k-1)
 			{
 				cout<<"Case #"<<m<<": IMPOSSIBLE\n";
 			}
 			else
 			{
 				cout<<"Case #"<<m<<": ";
 				for(ll co=2;co<=k;++co)
 				{
 					cout<<co<<" ";
 				}
 				cout<<endl;
 			}
 		}
 	} 
    return 0;
}
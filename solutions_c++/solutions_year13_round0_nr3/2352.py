//*****Template*****//
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <cstdio>
#include <string>
#include <cmath>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <stack>
#include <utility>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <numeric>
#include <iterator>
#include <functional>

#define INF 987654321
#define ll long long
#define rep0N(i,n) for(int i = 0;i < n;i++)
#define repN0(i,n) for(int i = n-1;i >= 0;i--)
#define repij(i,j,n) for(int i = j;j < n;i++)
#define pb(a) push_back(a)
#define si(a) scanf("%d",&a)
#define pi(a) printf("%d",a)

typedef struct node{
    int x;
    int y;
}node;

using namespace std;

int main(){
     long long int test,kutta,dick,chut,muth;
	 kutta = dick = 0;
     long long int j,A,B;
     long long int Arr[] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004};
     cin>>test;
     while(test--){
		vector<int>V1,V2;
        vector<vector<int> >V4;
        dick++;
        cin>>A>>B;
        kutta = 39;
        if(A > Arr[kutta-1]){
			cout<<0<<endl;
            continue;
        }
        if(B > Arr[kutta-1])
			B = Arr[kutta-1];
            for(int i = 0;i < kutta;i++){
				if(Arr[i] >= A){
					chut = i;
                    break;
				}
            }
            for(int i = 0;i < kutta;i++){
				if(Arr[i] <= B)
					muth = i;
            }
            cout<<"Case #"<<dick<<": "<<muth-chut+1<<endl;
     }
     return 0;
}


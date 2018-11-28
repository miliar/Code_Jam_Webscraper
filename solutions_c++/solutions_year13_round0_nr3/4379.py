#include<cstring>
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<map>
#include<list>
#include<vector>
#include <utility>
using namespace std;
int main(){
     long long int test_case,k_var,d,minx,maxx;
	 k_var = d = 0;
     long long int j,a_a,b_b;
     long long int v[] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004};
     cin>>test_case;
     while(test_case--){
        d++;
        cin>>a_a>>b_b;
        k_var = 39;
        if(a_a > v[k_var-1]){
			cout<<0<<endl;
            continue;
        }
        if(b_b > v[k_var-1])
			b_b = v[k_var-1];
            for(int i = 0;i < k_var;i++){
				if(v[i] >= a_a){
					minx = i;
                    break;
				}
            }
            for(int i = 0;i < k_var;i++){
				if(v[i] <= b_b)
					maxx = i;
            }
            cout<<"Case #"<<d<<": "<<maxx-minx+1<<endl;
     }
     return 0;
}
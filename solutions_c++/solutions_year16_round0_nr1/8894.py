#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <cmath>
#define s(a) scanf("%d",&a);
#define s2(a,b) scanf("%d %d",&a,&b);
#define sc(a) cin >> a;
#define sp(b) cout << b << "\n";
#define p(a) printf("%d\n",a);
#define p2(a,b) printf("%d %d",a,b);
#define pm(a) printf("a\n");
#define test(t) while(t>0)
#define sl(a) a.length();
#define f(a,b,c) for(a=b;a<c;a++)
#define v(a,b) vector<a> b;
#define pb(a,b) a.push_back(b);
#define ll long long
#define max(a,b) (abs(a)>abs(b) ? abs(a):abs(b))
#define min(a,b) (abs(a)<abs(b) ? abs(a):abs(b))
#define diff(a,b) abs(a-b);
int numofdigits(int x){

    if (x >= 10000) {
        if (x >= 10000000) {
            if (x >= 100000000) {
                if (x >= 1000000000)
                    return 10;
                return 9;
            }
            return 8;
        }
        if (x >= 100000) {
            if (x >= 1000000)
                return 7;
            return 6;
        }
        return 5;
    }
    if (x >= 100) {
        if (x >= 1000)
            return 4;
        return 3;
    }
    if (x >= 10)
        return 2;
    return 1;
}
ll pass(int number ,bool a[10],int count){
    bool flag=false;
    int i,j,k;
    count=0;
    ll temp,temp1,temp2=number,temp3=number;
    while(flag!=true){
        temp2=temp3;
        temp=numofdigits(temp2);
        f(i,0,temp){
            temp1 = temp2%10;
            if(a[temp1]==false){
                a[temp1]=true;
                count ++;
                if(count==10){
                    flag=true;
                    break;
                }
            }
            temp2 =temp2/10;
        }
        if(flag!=true){
            temp3 +=number;
        }
    }
    return temp3;
}
ll testing(int number){
    bool a[10]={0};
    int answer;
     int count=0;
    answer=pass(number,a,count);
    return answer;
}
using namespace std;
int main(){
	int t,n,i,j,x;
    ll answer;
	s(x);
    t=x;
	test(t){
		s(n);
        if(n!=0){
        answer=testing(n);
        }
        else{
            answer=0;
        }
        if(answer!=0){
            printf("Case #%d: %lld\n",x-t+1,answer);
        }
        else{
            printf("Case #%d: INSOMNIA\n",x-t+1);
        }
	t--;
	}	
}

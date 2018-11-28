//
//  main.cpp
//  GCJ_Q_C
//
//  Created by Ningchen Ying on 4/13/13.
//  Copyright (c) 2013 Ningchen Ying. All rights reserved.
//

/*
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <set>
using namespace std;

int id[200];
int mark[200];
long long h[1000]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
/*
bool check(long long h){
    int j;
    for(j=0;h!=0;j++){
        id[j]=h%10;
        h/=10;
    }
    j--;
    //cout<<j<<endl;
    int f=1;
    for(int k=0;k<=(j+1)/2 && f;k++){
        if(id[k]!=id[j-k]) return false;;
    }
    return true;
}
void deal(){
    int ans=0;
    for(int i=1;i<=10000000;i++){
        if(!check(i)) continue;
        long long h=(long long)i*(long long)i;
        //cout<<h<<endl;
        int j;
        for(j=0;h!=0;j++){
            id[j]=h%10;
            h/=10;
        }
        j--;
        //cout<<j<<endl;
        int f=1;
        for(int k=0;k<=(j+1)/2 && f;k++){
            if(id[k]!=id[j-k]) f=0;
        }
        h=(long long)i*(long long)i;
        if(f) cout<<h<<",";
    }
    //cout<<ans<<endl;
}*/
/*
int main(int argc, const char * argv[])
{
    //freopen("A.in","r",stdin);
	freopen("/Users/YNingC/Documents/CodeForces/GCJ_Q_C/GCJ_Q_C/C-large-1.in","r",stdin);
    freopen("/Users/YNingC/Documents/CodeForces/GCJ_Q_C/GCJ_Q_C/C-large-1.out","w",stdout);
	//freopen("/Users/YNingC/Documents/CodeForces/GCJ_Q_C/GCJ_Q_C/C-small-attempt0.in","r",stdin);
    //freopen("/Users/YNingC/Documents/CodeForces/GCJ_Q_C/GCJ_Q_C/C-small-attempt0.out","w",stdout);
    //deal();
    int T;
    long long M,N;
    cin>>T;
    for(int ca=1;ca<=T;ca++){
        cin>>N>>M;
        int ans=0;
        for(int p=0;p<39;p++){
            if(h[p]>=N && h[p]<=M) ans++;
        }
        printf("Case #%d: %d\n",ca,ans);
        //else printf("Case #%d: NO\n",ca);
    }
    
    return 0;
}
*/

/*
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <memory.h>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

#define MAX 10001

char sa[MAX],sb[MAX] ;
int res=0;

int bigchenfa(int *sum,int *a,int *b,int lsum,int la,int lb)
{
    int i,j;
    memset(sum,0,sizeof(sum));
    lsum = 0 ;
    for(i=1 ; i<= la ; i++) //用数组模拟运算
        for(j=1,lsum=i-1; j<= lb ; j++)
            sum[++lsum] += b[j] * a[i] ;
    
    for(i=1 ; i<= lsum ; i++)//进位处理
        if (sum[i] >= 10)
        {
            if ( sum[lsum] >= 10)
                lsum ++ ;
            sum[i+1] += sum[i] / 10 ;
            sum[i] %= 10 ;
        }
    
    return lsum ;
}

void solve(int la){
    int a[MAX]={0},b[MAX]={0},sum[MAX*2]={0} ;
    int lsum=0;
    //la = (int)strlen(sa);
    int i,j;
    for(i=1,j=la-1;i<= la ; i++,j--){
        a[i] = sa[j]-'0';
        b[i] = a[i];
    }
    lsum = bigchenfa(sum,a,b,lsum,la,la);
    int h=lsum/2;
    bool flag=true;
    for(int i=1;i<=h && flag;i++){
        if(sum[i]!=sum[lsum+1-i]) flag=false;
    }
    if(flag){
        res++;
        for(int i=1;i<=lsum;i++){
            printf("%d",sum[i]);
        }printf(",\n");
    }
}

void dfs(int h,int p){
    if(h+h+2>p+1){
        for(int i=0;i<h;i++){
            sa[p-i-1]=sa[i];
        }
        //cout<<sa<<endl;
        solve(p);
        return;
    }
    if(h==0){
        for(int i=1;i<=2;i++){
            sa[h]=i+'0';
            dfs(h+1,p);
        }
    }else{
        if(p%2==1 && h==p/2){
            for(int i=0;i<=2;i++){
                sa[h]=i+'0';
                dfs(h+1,p);
            }
        }else{
            for(int i=0;i<=1;i++){
                sa[h]=i+'0';
                dfs(h+1,p);
            }
        }
    }
    return;
}

int main()
{/*
    freopen("/Users/YNingC/Documents/CodeForces/GCJ_Q_C/GCJ_Q_C/ans.txt","w",stdout);
    cout<<"1"<<endl;
    cout<<"4"<<endl;
    cout<<"9"<<endl;
    for(int i=2;i<=50;i++){
        dfs(0,i);
    }
    cout<<"-----------"<<endl;
    cout<<res<<endl;
    ifstream myfile;
    //freopen("ActivePoint.txt","w",stdout);
	myfile.open ("/Users/YNingC/Documents/GBPM_tree/GBPM_3D/GBPM_3D/ActivePoint.txt");
    string s;
    while(myfile>>s){
        cout<<s<<endl;
    }
	myfile.close();
    return 0 ;
}*/

#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <set>
using namespace std;
string ans[60000];
int n;
int compare(string a,string b){
	if(a.length()!=b.length()){
        return a.length()>b.length();
    }
	return a>=b;
}
int binary_calc(string node,int &f){
	int L=1,R=n;
	int ret=0;
	while(L<=R){
		int mid=(L+R)/2;
		if(compare(node,ans[mid])>0){
			ret=mid;
			L=mid+1;
		}else R=mid-1;
	}
	if(ans[ret]==node) f=1;
	else f=0;
	return ret;
}
int main()
{
	freopen("/Users/YNingC/Documents/CodeForces/GCJ_Q_C/GCJ_Q_C/ans.txt","r",stdin);
    ifstream myfile;
    myfile.open("/Users/YNingC/Documents/CodeForces/GCJ_Q_C/GCJ_Q_C/ans.txt");
	n=0;
	while(myfile>>ans[++n]);
    myfile.close();
    //cout<<ans[n-3]<<endl;
	n-=3;
	freopen("/Users/YNingC/Documents/CodeForces/GCJ_Q_C/GCJ_Q_C/C-large-2.in","r",stdin);
	freopen("/Users/YNingC/Documents/CodeForces/GCJ_Q_C/GCJ_Q_C/C-large-2.out","w",stdout);
    int T;
	cin>>T;
	for(int ca=1;ca<=T;ca++){
        string X,Y;
        char s1[110],s2[110];
		scanf("%s%s",s1,s2);
		X=s1;
        Y=s2;
		int f;
		int res=binary_calc(Y,f)-binary_calc(X,f)+f;
		printf("Case #%d: %d\n",ca,res);
	}
	return 0;
}

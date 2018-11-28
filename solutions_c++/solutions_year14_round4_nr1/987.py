#include <iostream>
#include <string>
#include<cmath>
#include <fstream>
 #include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <ctime>
using namespace std;

class tou{
    friend bool operator<=(tou x,tou y){return x.b<=y.b;}
    friend bool operator>=(tou x,tou y){return x.b>=y.b;}
public:int b;
};

int divide(int  a[],int low,int high){
	int k=a[low];
	do {while (low<high&&a[high]>=k)--high;
	if(low<high){a[low]=a[high];++low;}
	while (low<high&&a[low]<=k)++low;
	if(low<high){a[high]=a[low];--high;}
	}while (low!=high);
	a[low]=k;
	return low;
}
void quicksort(int a[],int s,int e){
	if(s>=e)return ;
	int mid=divide(a,s,e);
	quicksort(a,s,mid-1);
	quicksort(a,mid+1,e);
}
class node{
    public:
    int b;
    node *next;
    node(){b=0;next=NULL;}
};
int main(){
    ifstream cin("ia.in");
    ofstream cout("oa.out");
 int t;
   cin>>t;
   for(int round=1;round<=t;++round){
           int n,l, *a;
        cin>>n>>l; a=new int[n+10];
        for(int i=0;i<n;++i)cin>>a[i];
        quicksort(a,0,n-1);
        int qi=0, zh=n-1,ans=0;
        while(qi<=zh){
            if(qi==zh){++ans;++qi;}
            else if(a[qi]+a[zh]<=l){++ans;++qi;--zh;}
            else {++ans;--zh;}
        }
        cout<<"Case #"<<round<<": ";
        cout<<ans<<endl;
   }
return 0;
}

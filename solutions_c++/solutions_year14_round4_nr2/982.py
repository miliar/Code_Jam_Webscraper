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
    ifstream cin("ic.in");
    ofstream cout("oc.out");
 int t;
   cin>>t;
   for(int round=1;round<=t;++round){
        int ans=0;
        int n;
        cin>>n;
        int a[1005];
        for(int i=0;i<n;++i)cin>>a[i];
        for(int i=0;i<n;++i){   //n-i  ge shu
            int min=0;
            for(int j=1;j<n-i;++j) if(a[j]<a[min])min=j;
            ans+=(n-i-1-min)<min?(n-i-1-min):min;
            for(int j=min;j<n-i-1;++j) a[j]=a[j+1];
        }
        cout<<"Case #"<<round<<": "<<ans<<endl;
   }
return 0;
}

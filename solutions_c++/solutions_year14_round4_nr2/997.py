#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int cas, num, ans;
int arr[1024];
int flg[1024];

int check() {
  int i;
  for (i=1; i<num; ++i) {
    if (arr[i]<arr[i-1]) break;
  }
  for (i; i<num; ++i) {
    if (arr[i]>arr[i-1]) return 0;
  }
  return 1;
}

int ck1(int st, int ed) {
  for (int i=st+1; i<=ed; ++i) {
    if (arr[i]<arr[i-1]) return 0;
  }
  return 1;
} 

int ck2(int st, int ed) {
  for (int i=st+1; i<=ed; ++i) {
    if (arr[i]>arr[i-1]) return 0;
  }
  return 1;
}

void sp(int i, int j) {
  int tmp=arr[i];
  arr[i]=arr[j];
  arr[j]=tmp;
}

int sol() {
  int minn=2147483647, mid=-1, mv1, mv2;
  for (int i=0; i<num; ++i) if (!flg[i]) {
    if (minn>arr[i]) {
      minn=arr[i]; mid=i;
    }
  }
  if (mid==-1) {cout<<"error\n"; return 0;}
  mv1=mv2=0;
  for (int i=mid-1; i>=0; --i)
    if (!flg[i]) {++mv1;}
    else break;
  for (int i=mid+1; i<num; ++i)
    if (!flg[i]) {++mv2;}
    else break;

  if (mv1<=mv2) {
    if (ck1(0,mid)) {flg[mid]=1; return 1;}
    for (mid; mid>0 && !flg[mid-1]; --mid) {sp(mid-1, mid); ++ans;}
    flg[mid]=1;
  }
  else {
    if (ck2(mid,num-1)) {flg[mid]=1; return 1;}
    for (mid; mid+1<num && !flg[mid+1]; ++mid) {sp(mid, mid+1); ++ans;}
    flg[mid]=1;
  }
  return 1;
}

int main() {
  scanf("%d",&cas);
  for (int k=1; k<=cas; ++k) {
    scanf("%d",&num);
    for (int i=0; i<num; ++i) {
      scanf("%d",&arr[i]); flg[i]=0;
    }
    ans=0;
    while (!check()) {
      if (!sol()) break;
      //cout<<ans<<endl;
      //for (int i=0; i<num; ++i) cout<<arr[i]<<" "; cout<<endl;
    }
    printf("Case #%d: %d\n",k,ans);
  }
  return 0;
}

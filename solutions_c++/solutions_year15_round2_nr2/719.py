#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int t;
int main(){
scanf("%d",&t);
int npb;
int w[16];

for(int npb=1;npb<=t;npb++){
int r,c,n;
scanf("%d%d%d",&r,&c,&n);
for(int i=0;i<(r*c)-n;i++)w[i]=0;
for(int i=(r*c)-n;i<r*c;i++)w[i]=1;
int msol=420;
int ct=0;
do {//ct++;printf("%d\n",ct);
    int sol=0;
    for(int i=0;i<r;i++)
    for(int j=0;j<c;j++){
    if(w[j*r+i]){
     if(i>0 && w[j*r+i-1] )sol++;
     if(i<r-1 && w[j*r+i+1])sol++;
     if(j>0 && w[(j-1)*r+i])sol++;
     if(j<c-1 && w[(j+1)*r+i])sol++;
    }
    }
    if(msol>sol)msol=sol;
} while ( std::next_permutation(w,w+(r*c)) );
msol/=2;
printf("Case #%d: %d\n",npb,msol);
}
return 0;
}

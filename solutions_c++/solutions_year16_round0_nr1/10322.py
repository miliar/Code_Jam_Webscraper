#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int main(){
long long unsigned int t,i,j,n,ans=0;
FILE *fp = fopen("input.txt","r");
FILE *ft = fopen("output.txt","w");
fscanf(fp,"%llu", &t);
int c=t;
while(t--){
ans=0;
int arr[10] = {0};
int cnt=0;

fscanf(fp, "%llu", &n);
while(n!=0 && cnt!=10){
i = n * (++ans);
while(i!=0){
j = i%10;
i=i/10;

if(arr[j] == 0){
  cnt++;
arr[j] = 1;
}

}
}

fprintf(ft, "Case #%d: ",c-t);
if(cnt!=10)
  fprintf(ft, "%s\n", "INSOMNIA");
else
  fprintf(ft, "%llu\n",n *ans);




}


return 0;
}

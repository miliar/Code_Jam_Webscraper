#include <cstdio>
#include <algorithm>

using namespace std;

long long data_set[]={0,1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004,100000020000001};

int main(){
FILE* in;
FILE* out;

in=fopen("C-large-1.in","r");
out=fopen("ouput.in","w");

int t=0;
long long min=0,max=0,soln=0;
fscanf(in,"%d",&t);
for(int i=1;i<=t;i++){
    fscanf(in,"%llu",&min);
    fscanf(in,"%llu",&max);
    for(int j=0;j<41;j++){
        if(data_set[j]>=min&&data_set[j]<=max){
            soln++;
        }
    }
    fprintf(out,"Case #%d: %d\n",i,soln);
    soln=0;
}

fclose(in);
fclose(out);
}

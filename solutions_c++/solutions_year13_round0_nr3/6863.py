#include <iostream>
#include <cstdio>
#include <cassert>
using namespace std;

#define N 10000
typedef long long LL;
bool isfair(LL num){
    LL r=0,temp=num;
    while(temp){
        r=r*10+temp%10;
        temp/=10;
    }
    return r==num;
}

LL fsqf[N];
int n;

int pos(LL value,bool &flag){
    int left=0;int right=n;
    flag=false;
    if(value<fsqf[0]){
        return 0;
    }
    if(value>fsqf[n-1]){
        return n;
    }
    while(left<right){
        int middle=left+((right-left)>>1);
        if(value < fsqf[middle]){
            right=middle;
        }else if(value > fsqf[middle]){
            left=middle+1;
        }else{
            flag=true;
            return middle;
        }
    }
    return left;
}

int main()
{
    FILE *in, *out;
	in = fopen("E:\\bing\\desktop\\C-small-attempt1.in","r");
	out = fopen("E:\\bing\\desktop\\C-small-attempt1.out","w");

    int T;
    LL ii=0;
    for(int i=1;ii<=1000;++i){
        ii=i*i;
        if(isfair(i) && isfair(ii)){
            fsqf[n++]=ii;
        }
    }
    #if 0
    for(int i=0;i<n;++i){
        printf("%I64d ",fsqf[i]);
    }
    printf("\n%d\n",pos(1));
    #endif
    fscanf(in,"%d",&T);
    for(int i=1;i<=T;++i){
        LL a,b;
        fscanf(in,"%I64d %I64d",&a,&b);
        bool found;
        int posa=pos(a,found);
        int posb=pos(b,found);//found = foundb
        if(found)
            posb++;
        fprintf(out,"Case #%d: %d\n",i,posb-posa);

    }
    fclose(in);
	fclose(out);
    return 0;
}

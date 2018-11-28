#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<map>

using namespace std;

bool chkdigit(map<int,bool> &a,int n) {
    while(n) {
        a.erase(n%10);
        n/=10;
        if(a.size()==0)
            return true;
    }
    return false;
}
int check(int n) {
    if(n==0) {
        //printf("INSOMNIA\n");
        return 0;
    }

    switch(n) {
        case 10:
        case 100:
        case 1000:
        case 10000:
        case 100000:
        case 1000000:
            return n*9;
    }

    map<int,bool> a;
    a[0]=true;
    a[1]=true;
    a[2]=true;
    a[3]=true;
    a[4]=true;
    a[5]=true;
    a[6]=true;
    a[7]=true;
    a[8]=true;
    a[9]=true;

    int k=n;
    for(int i=1;;i++,n+=k) {
        if(chkdigit(a,n))
            break;
    }
    //printf("%d\n",n);
    return n;
}

int main() {
    int n,t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++) {
        scanf("%d",&n);
        printf("Case #%d: ",i);
        int res=check(n);
        if(res==0)
            printf("INSOMNIA\n");
        else
            printf("%d\n",res);
    }
}

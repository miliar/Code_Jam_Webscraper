#include<bits/stdc++.h>
#define MAX 1001

using namespace std;

typedef long long llong;
class Sample {
public:
    string x;
    int factor[11];
};
bool p[MAX];
vector <int> prime;
void initializer() {
    int i,j;
    for(i=2;i*i<MAX;i++)
        if(!p[i])
            for(j=i*i;j<MAX;j+=i)
                p[j]=true;
    for(i=2;i<MAX;i++)
        if(!p[i])
            prime.push_back(i);
}
int power(int base,int index,int m) {
    if(!index)
        return 1;
    llong temp=power(base,index>>1,m);
    temp=(temp*temp)%m;
    if(index&1)
        temp=(base*temp)%m;
    return temp;
}
bool mod_func(string &x,int base,int m) {
    int i,p=0;
    int modv=0;
    for(i=x.size()-1;i>=0;i--,p++) {
        if(x[i]=='1') {
            modv=(power(base,p,m)+modv)%m;
        }
    }
    return modv==0;
}
bool is_prime_in_base(string &x,int base) {
    int i,po=0,n=0;
    for(i=x.size()-1;i>=0 && n<MAX;i--,po++) {
        if(pow(base,po)>=MAX)
            return false;
        if(x[i]=='1')
            n+=pow(base,po);
    }
    if(n<MAX) {
        return !p[n];
    }
    return false;
}
bool fun(string &x,Sample a[],int ind) {
    a[ind].x=x;
    int i,j;
    for(i=2;i<11;i++) {
        if(is_prime_in_base(x,i))
            return false;
        for(j=0;j<prime.size();j++) {
            int m=prime[j];
            if(mod_func(x,i,m)) {
                a[ind].factor[i]=m;
                break;
            }
        }
        if(j==prime.size())
            return false;
    }
    return true;
}
int main() {

    freopen("C:\\Users\\Saurabh\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Users\\Saurabh\\Desktop\\out.txt","w",stdout);

    initializer();
    srand(time(NULL));
    int t,cas=1;
    cin>>t;
    while(t--) {
        int n,J,c=0,i,j;
        map <string,bool> m;
        cin>>n>>J;
        Sample a[J];
        string x="1";
        for(i=0;i<n-2;i++)
            x+='0';
        x+='1';
        if(fun(x,a,c))
            c++;
        m[x]=true;
        while(c<J) {
            for(i=1;i<n-1;i++) {
                x[i]=(rand()&1)+'0';
            }
            if(m[x])
                continue;
            m[x]=true;
            if(fun(x,a,c))
                c++;
        }
        cout<<"Case #"<<cas++<<": \n";
        for(i=0;i<J;i++) {
            cout<<a[i].x<<" ";
            for(j=2;j<11;j++) {
                cout<<a[i].factor[j]<<" ";
            }
            cout<<endl;
        }
    }

    return 0;
}

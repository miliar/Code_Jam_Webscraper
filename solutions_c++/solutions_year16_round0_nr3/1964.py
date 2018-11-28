#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

# define ull unsigned long long

 ofstream g;
ull myPow(ull x, ull p)
{
    if (p == 0) return 1;
    if (p == 1) return x;

    ull tmp = myPow(x, p/2);
    if (p%2 == 0) return tmp * tmp;
    else return x * tmp * tmp;
}
void kiir(vector<int> v)
{
    for(int i=0; i<v.size(); ++i)
    {
        cout<<v[i];
    }
    cout<<endl;
}

bool prim(ull a, ull &b)
{
    if(a%2==0)
    {
        b=2;
        return false;
    }
    for(ull i=3; i*i<=a; i=i+2)
    {
        if(a%i==0)
        {
            b=i;
            return false;
        }
    }
    return true;
}





ull szamma (ull b, vector<bool> v)
{
    ull sz=0;
    for(int i=0; i<16; ++i)
    {
        if(v[i]) sz+=myPow(b,15-i);

    }
    return sz;
}

void szorzat(vector<int> &v, int a)
{
    if(a==10)
    {
        v.push_back(0);
    }
    else
    {
        int m=0;
        int i=v.size()-1;
        while(i>=0)
        {
            int temp=v[i]*a+m;
            v[i]=temp%10;
            m=temp/10;
            i--;
        }
        if(m!=0)
        {
            vector<int>::iterator it=v.begin();
            it = v.insert ( it, m );
        }
    }
}

vector<int> osszead(vector<int> v1, vector<int> v2)
{
 vector<int> v3(max(v1.size(),v2.size()));
 int m=0;
 if(v1.size() <v2.size())
 {
     vector<int>::iterator it=v1.begin();
     v1.insert (it,v2.size()-v1.size(),0);
 }
 if(v1.size() > v2.size())
 {
     vector<int>::iterator it=v2.begin();
     v2.insert (it,v1.size()-v2.size(),0);
 }
 int i=v1.size()-1;
 while(i>=0)
 {
     int temp=v1[i]+v2[i]+m;
     v3[i]=temp%10;
     m=temp/10;
     i--;
 }
  if(m!=0)
        {
            vector<int>::iterator it=v3.begin();
            it = v3.insert ( it, m );
        }
 return v3;
}

vector<int> vektorra (ull b, vector<bool> v)
{
vector<int> vissza;
for(int i=v.size()-1; i>=0; --i)
{
    if(v[i])
    {
        vector<int> t(1,1);
        for(int j=0; j<v.size()-1-i; ++j) {szorzat(t,b);}
        vissza=osszead(vissza,t);
    }
}
//cout<<b<<"   "; kiir(vissza);
return vissza;

}


void kiir(vector<bool> v,vector<ull> biz)
{
    for(int i=0; i<v.size(); ++i)
    {
        if(v[i])cout<<"1";
        else cout<<"0";
    }
    for(int i=0; i<9; ++i)
    {
        cout<<" "<<biz[i];
    }
    cout<<endl;

}
void kiirFajl(vector<bool> v,vector<ull> biz)
{
    for(int i=0; i<v.size(); ++i)
    {
        if(v[i]) g<<"1";
        else g<<"0";
    }
    for(int i=0; i<9; ++i)
    {
        g<<" "<<biz[i];
    }
    g<<endl;

}

void kiir(vector<bool> v)
{
    for(int i=0; i<v.size(); ++i)
    {
        if(v[i])cout<<"1";
        else cout<<"0";
    }
    cout<<endl;
}


void leptet (vector<bool> &v)
{
    int c=0;
    int i=v.size()-2;
    while(v[i])
    {
        i--;
        c++;
    }

    v[i]=true;
    for(int j=i+1; j<31; ++j)
        v[j]=false;

}

bool oszthato (vector<int> sz, int a)
{
    int m=0;
    for(int i=0; i<sz.size(); ++i)
    {
        m=(m*10+sz[i])%a;
    }
    return (m==0);
}

bool prim2(vector<int> sz, ull &b)
{
    if(sz[sz.size()-1]%2==0) {b=2; return false;}
    for(int i=3; i<1000; i=i+2)
    {
        if(oszthato(sz,i)) {b=i; return false;}
    }
    return true;
}


int main()
{

    string gname="ki2.txt";
    g.open(gname.c_str());
//500 db 32 hosszú coinjam
    int c=0;
    vector<bool> v(32,false);
    v[0]=true;
    v[31]=true;
    while(c!=500)
    {
        vector<ull> biz(9,-1);
        ull b=2;
        while(b<=10)
        {
            if(prim2(vektorra(b,v),biz[b-2])) break;
            b++;
        }

        if(b==11)
        {
            c++;
            kiir(v,biz);
            kiirFajl(v,biz);
        }

        leptet(v);
    }




    return 0;
}

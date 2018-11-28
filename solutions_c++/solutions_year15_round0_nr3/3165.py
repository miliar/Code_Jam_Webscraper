#include <iostream>
#include <bits/stdc++.h>
using namespace std;
class Vector{
public:
    int f[4];
    Vector(int a,int b,int c,int d)
    {
        f[0]=(a);
        f[1]=(b);
        f[2]=(c);
        f[3]=(d);
    }
    Vector operator*(const Vector &b) const
    {
        Vector v(0,0,0,0);
        v.f[0] = f[0]*b.f[0]-f[1]*b.f[1]-f[2]*b.f[2]-f[3]*b.f[3];
        v.f[1] = f[0]*b.f[1]+ f[1]*b.f[0] + f[2]*b.f[3]-f[3]*b.f[2];
        v.f[2] = f[0]*b.f[2] - f[1]*b.f[3]+f[2]*b.f[0] + f[3]*b.f[1];
        v.f[3] = f[0]*b.f[3] + f[1]*b.f[2] -f[2]*b.f[1]+ f[3]*b.f[0];
        return v;

    }
    Vector operator-() const
    {
        Vector v(0,0,0,0);
        for(int i=0;i<4;++i)
            v.f[i] = -f[i];
        return v;
    }
    bool operator[](int i)
    {
        return f[i];
    }
    bool operator==(const Vector &b) const
    {
        for(int i=0;i<4;++i)
            if(f[i]!=b.f[i])
                return false;
        return true;
    }
    Vector operator/(const Vector &b) const
    {
        return (*this)*b;

    }
    bool operator!=(const Vector &b) const
    {
        return !((*this) == b);
    }
    friend ostream &operator<<(ostream &output,const Vector &b)
    {
        for(int i=0;i<4;++i)
            output<<b.f[i]<<" ";
        return output;

    }

    Vector()
    {

    }
};
Vector cumForward[10003];
Vector cumBackward[10003];
map<char,Vector> mp;

int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);

    Vector i(0,1,0,0);
    Vector j(0,0,1,0);
    Vector k(0,0,0,1);
    Vector _1(1,0,0,0);
    mp['i'] = i;
    mp['j'] = j;
    mp['k'] = k;
    mp['1'] = _1;

    int t; cin>>t;
    for(int kase = 1;kase<=t;++kase)
    {
        vector<int> iindices,kindices;

        int l,x;
        cin>>l>>x;
        string s; cin>>s;
        string fin="";
        for(int i=1;i<=x;++i)
            fin+=s;
        Vector curr = _1;
        for(int ii=0;ii<fin.size();++ii)
        {
            char c = fin[ii];
            Vector m = mp[c];
            curr = (curr*m);
            cumForward[ii] = curr;
            if(curr == i)
            {
                iindices.push_back(ii);
            }
        }
        curr = _1;
        for(int ii=fin.size()-1;ii>=0;--ii)
        {
            char c=fin[ii];
            Vector m = mp[c];
            curr = (m*curr);
            cumBackward[ii] = curr;
            if(cumBackward[ii] == k)
                kindices.push_back(ii);
        }
        bool res = false;
        for(int fi=0;fi<iindices.size();++fi)
        {
            for(int bi=0;bi<kindices.size();++bi)
            {
                if(iindices[fi]>=kindices[bi])
                    break;
                int r = kindices[bi]-1;
                int l = iindices[fi];
                Vector a = -cumForward[l];
                Vector c = cumForward[r];
                if((a*c) == j)
                    res = true;
            }

        }





        cout<<"Case #"<<kase<<": "<<(res?"YES":"NO")<<"\n";


    }
}

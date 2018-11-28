#include<iostream>
#include<string.h>
using namespace std;
#define ll long long


struct vec {
    char meg;
    int sign;
};

int ind (vec *x)  {
    if (x->meg=='1')
        return 0;
    else return x->meg -'h';
}



char str[10003];
char str2[10003];

vec cross [4][4] {  { {'1',1}, {'i',1}, {'j',1}, {'k',1} } ,
                    { {'i',1}, {'1',-1}, {'k',1}, {'j',-1} } ,
                    { {'j',1}, {'k',-1}, {'1',-1}, {'i',1} } ,
                    { {'k',1}, {'j',1}, {'i',-1}, {'1',-1} }

};




void  get_cross(vec* a,vec* b, vec* res) {
    int sign = a->sign * b->sign;

    *res = cross [ind(a)][ind(b)];
    res->sign = res->sign * sign;


}
int main () {


    int t;
    cin>>t;
    ll l,x;
    for (int i=1;i<=t;i++) {
        cin>>l>>x;
        cin>>str2;
        vec  res = {str2[0],1};
        int z=1;
        vec b;
        vec word ={str[0],1};
        int j_start,j_end;
        vec temp;
        strcpy (str,str2);

        for (int j=1;j<x;j++) {
            strcat(str,str2);
        }
        //cout<<endl<<str<<endl;
        z=1;
        l*=x;
        while (z<l&& (res.meg != 'i' || res.sign !=1)) {
            b.meg= str[z];
            b.sign=1;
            //cout<<res.meg<<b.meg<<endl;
            get_cross(&res,&b,&temp);
            res =temp;
            //cout<<" meg="<<res.meg<<" sign="<<res.sign<<endl;
            z++;
        }

        if (z==l)  {
            cout<<"Case #"<<i<<": "<<"NO\n";
            continue;
        }
//cout<<"hi\n";
        res.meg=str[z];
        res.sign=1;
        z++;
        while (z<l&& (res.meg != 'j' || res.sign !=1 )) {
            b.meg= str[z];
            b.sign=1;
            get_cross(&res,&b,&temp);
            res =temp;
            z++;
        }

        if (z==l)  {
            cout<<"Case #"<<i<<": "<<"NO\n";
            continue;
        }
    //cout<<"hi\n";
        res.meg=str[z];
        res.sign=1;
        z++;
        while (z<l) {
            b.meg= str[z];
            b.sign=1;
            get_cross(&res,&b,&temp);
            res =temp;
            z++;
        }

        if (res.meg!='k'||res.sign !=1)  {
            cout<<"Case #"<<i<<": "<<"NO\n";
            continue;
        }


        cout<<"Case #"<<i<<": "<<"YES\n";
    }
    return 0;
}

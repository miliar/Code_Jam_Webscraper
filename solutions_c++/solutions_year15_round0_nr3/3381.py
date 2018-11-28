#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;

ifstream in("INPUT.TXT ");
ofstream out("OUTPUT.TXT");



class quat
{
public:
    quat(const char ch);
    quat(const int ii,const int ij,const int ik,const int id);
    quat operator *(quat q);


public:
    int i;
    int j;
    int k;
    int d;

};

std::ostream& operator<<(std::ostream& os, const quat& q);

quat::quat(const char ch)
{
    if (ch == 'i'){i = 1;j = 0;k = 0; d = 0;}
    else if (ch == 'j'){i = 0;j = 1; k = 0; d = 0;}
    else if (ch == 'k'){i = 0;j = 0;k = 1; d = 0;}
    else {i = j = k = d = 0;}
}

quat::quat(const int ii,const int ij,const int ik,const int id)
{
    i = ii;
    j = ij;
    k = ik;
    d = id;
    //cout<<"constr    "<<i<<"  "<<j<<"   "<<k<<"   "<<d<<endl;
}

quat quat::operator*(quat q)
{
    quat* q1 = this;
    quat* q2 = &q;
    int ii = q1->i*q2->d + q1->j*q2->k - q1->k*q2->j + q1->d*q2->i;
    int ij = -q1->i*q2->k + q1->j*q2->d + q1->k*q2->i + q1->d*q2->j;
    int ik = q1->i*q2->j - q1->j*q2->i + q1->k*q2->d + q1->d*q2->k;
    int id = -q1->i*q2->i - q1->j*q2->j - q1->k*q2->k + q1->d*q2->d;

    //cout<<ii<<"  "<<ij<<"   "<<ik<<"   "<<id<<endl;
    quat out(ii,ij,ik,id);

    return out;

}

std::ostream& operator<<(std::ostream& os, const quat& q)
{
    os<<q.i<<"i";
    os<<q.j<<"j";
    os<<q.k<<"k";
    os<<q.d<<"d";
  // write obj to stream
  return os;
}

bool isGood(const char* buff, int l, int L)
{
    quat qi(buff[0]);
    for (int il = 1;il<l;il++) // find i
    {

        if (qi.i != 1)
        {
            qi = qi*quat(buff[il%L]);
            continue;
        }
        //cout<<"il "<<il<<"qi  "<<qi.i<<endl;
        int ij = il;
        quat qj(buff[ij%L]);
        for (;ij<l;ij++)
        {
            if (qj.j != 1)
            {
                qj = qj*quat(buff[ij%L]);
                continue;
            }
            //cout<<"ij "<<ij<<"qj  "<<qj.j<<endl;
            int ik = ij+1;
            quat qk(buff[ik%L]);
            //cout<<"ik "<<ik<<"qk "<<qk<<endl;
            for (ik++;ik<l;ik++)
            {
                qk = qk*quat(buff[ik%L]);//cout<<"qk "<<qk<<" "<<quat(buff[ik%L])<<" ("<<ik<< ") ";
            }
            //cout<<endl;
            if (qk.k == 1) return true;
            else{ ij++;
                if(ij<l) qj = qj*quat(buff[ij%L]);}

        }
        il++;
        if(il<l) qi = qi*quat(buff[il%L]);

    }
    return false;
}


int main ()
{
    int T;
    in >> T;
    int L,X,l;
    char buff[10010];
    //quat a('k'),b('j');
    //cout<<a<<"*"<<b<<"="<<a*b<<endl;
    //exit(0);
    for (int iT = 0; iT < T; iT++)
    {
        cout<<iT<<endl;
        in >> L;
        in >> X;
        l = L*X;
        in >> buff;
        bool GOOD = isGood(buff,l,L);
        out<<"Case #"<<iT+1<<": "<<(GOOD ? "YES" : "NO")<<endl;

    }


    return 0;
}


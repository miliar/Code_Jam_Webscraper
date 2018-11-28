#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
float * qsort(float in[],int len)
{
    float *new_in=new float[len];
    if(len>1)
    {
        int i=0,j=0,k=0;
        float *left=new float[len];
        float *right=new float[len];
        float piv=in[len-1];
        //cout<<endl<<piv<<endl;
        for(;k<len;k++)
        {
            if(k!=len-1)
            {
                if(in[k]<piv)
                {
                    left[i++]=in[k];
                }
                else
                {
                    right[j++]=in[k];
                }
            }
        }
       float *left_new=qsort(left,i);
       float *right_new=qsort(right,j);
       int l_index=0,r_index=0;
       for(k=0;k<len;k++)
       {
           if(k<i)
           {
               new_in[k]=left_new[l_index++];
           }
           else if(k==i)
           {
               new_in[k]=piv;
           }
           else
           {
               new_in[k]=right_new[r_index++];
           }
       }
       return new_in;
    }
    else
    {
        return in;
    }
}
int getDeceitWarWins(float *naomi,float *ken,int s)
{
    int count=0;
    for(int i=0,j=0;i<s;i++)
    {
        if(naomi[i]>ken[j])
        {
            count++;
            j++;
        }
    }
    return count;
}
int getWarWins(float *naomi,float *ken,int s)
{
    int count=0;
    for(int i=0,j=0;i<s;i++)
    {
        if(ken[i]>naomi[j])
        {
            count++;
            j++;
        }
    }
    return (s-count);
}
int main()
{
    float *ken,*naomi;
    int n,s;
    fstream fin;
    fin.open("D-large.in",ios::in);
    fin>>n;
    int index=1;
    while(index++<(n+1))
    {
        fin>>s;
        ken= new float[s];
        naomi= new float[s];
        for(int i=0;i<s;i++)
            fin>>naomi[i];
        for(int i=0;i<s;i++)
            fin>>ken[i];
        naomi=qsort(naomi,s);
        ken=qsort(ken,s);
        /*for(int i=0;i<s;i++)
        cout<<naomi[i]<<"   "<<ken[i]<<endl;*/
        int cd=getDeceitWarWins(naomi,ken,s);
        int cw=getWarWins(naomi,ken,s);
        fstream fout;
        fout.open("out.txt",ios::out|ios::app);
        fout<<"Case #"<<(index-1)<<": "<<cd<<" "<<cw<<endl;
        fout.close();
        //cout<<endl;
        delete ken;
        delete naomi;
    }
    fin.close();
}

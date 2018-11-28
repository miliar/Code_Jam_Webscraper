/*
 * =====================================================================================
 *
 *       Filename:  gcj2.cpp
 *
 *    Description:
 *
 *
 *        Version:  1.0
 *        Created:  Saturday 12 April 2014 11:53:44  IST
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  SUDARSHAN (),
 *   Organization:  BITS PILANI, HYDERABAD
 *
 * =====================================================================================
 */
#include<iostream>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<cmath>
#define min(a,b) (a<b?a:b)
using namespace std;
int main()
{

  FILE * pfile;
  FILE * output;

  //ofstream fout ("test.out");
  pfile= fopen("B-large.in","r");
  output=fopen("test3.out","w");
  int t;
  fscanf(pfile,"%d",&t);
  for (int ii=0;ii<t;ii++){
  double c,f,x,sum,curr,prev,n=2;
  fscanf(pfile,"%lf %lf %lf",&c,&f,&x);

        n=2;
        prev=x/2;
        sum=0;
        while(1)
        {
            sum+=c/n;
            //cout<<sum<<endl;
            n+=f;
            curr=sum+(x/n);
            //cout<<curr<<" "<<prev<<endl;
            if(curr>=prev)
                break;
            else
              {

                prev=curr;
              }

        }

 fprintf(output,"Case #""%d"": ""%.7lf\n",ii+1,prev);
 }
  return 0;
}


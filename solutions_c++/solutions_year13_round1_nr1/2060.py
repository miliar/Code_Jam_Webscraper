#include<iostream>
#include<algorithm>
#include<vector>
#include<fstream>
#include<string>
#include<stdio.h>
using namespace std;
template<class t>
void number_to_vector(t num,vector<int> &v1)
{
    while(num)
    {
        v1.push_back(num%10);
        num=num/10;
    }
    reverse(v1.begin(),v1.end());
}
void add_vector(vector<int>arr1,vector<int>arr2,vector<int>&ans)
{
    ans.clear();
    int flag=0;
    int index1,index2;
    if(arr1.size()==0)
    {
        ans.resize(arr2.size());
        copy(arr2.begin(),arr2.end(),ans.begin());
        return;
    }
    if(arr2.size()==0)
    {
        ans.resize(arr1.size());
        copy(arr1.begin(),arr1.end(),ans.begin());
        return;
    }
    index1=arr1.size()-1;
    index2=arr2.size()-1;
    //cout<<index1<<index2;
    if(index1>index2)
    {
       ans.resize(index1+2);
       copy(arr1.begin(),arr1.end(),ans.begin()+1);
    }
    if(index1<index2)
    {
        ans.resize(index2+2);

        copy(arr2.begin(),arr2.end(),ans.begin()+1);
        flag=1;

    }
    if(index1==index2)
    {
       ans.resize(index1+2);
       copy(arr1.begin(),arr1.end(),ans.begin()+1);


    }
    int ans_index=ans.size()-1,ans_index_temp;
    int temp;
    if(flag==0)
    {
        int debug;
       for(;index2>=0;index2--,ans_index--)
       {
          temp=arr2[index2]+ans[ans_index];
          //cout<<temp;
          //cin>>debug;
          ans_index_temp=ans_index;
          while(temp)
          {
             ans[ans_index_temp]=temp%10;
             temp=temp/10;
             if(ans_index_temp>0)
             {
             ans_index_temp--;
             temp=temp+ans[ans_index_temp];
             }
             else
             {
                break;
             }
          }
       }
    }
    else
    {

       for(;index1>=0;index1--,ans_index--)
       {
          temp=arr1[index1]+ans[ans_index];

          ans_index_temp=ans_index;
          while(temp)
          {
             ans[ans_index_temp]=temp%10;
             temp=temp/10;
              if(ans_index_temp>0)
             {
             ans_index_temp--;
             temp=temp+ans[ans_index_temp];
             }
             else
             {
                break;
             }
          }
       }
    }
    if(ans[0]==0)
    {
        for(vector<int>::iterator itf=ans.begin()+1,itb=ans.begin();itf!=ans.end();itf++,itb++)
            *itb=*itf;
        ans.resize(ans.size()-1);
    }

}
void vector_multiplication(vector<int>v1,vector<int>v2,vector<int>&ans)
{
    vector<int>ans_temp;
    int temp=0;
    int p=0;
    for(vector<int>::reverse_iterator v2it=v2.rbegin();v2it!=v2.rend();v2it++,p++)
    {
        temp=0;
        for(vector<int>::reverse_iterator v1it=v1.rbegin();v1it!=v1.rend();v1it++)
        {
          temp+=(*v1it)*(*v2it);
          ans_temp.push_back(temp%10);
          temp=temp/10;
        }
        if(temp)
        {
            ans_temp.push_back(temp);
        }
        reverse(ans_temp.begin(),ans_temp.end());
        for(int i=0;i<p;i++)
        {
            ans_temp.push_back(0);
        }
        add_vector(ans_temp,ans,ans);
        ans_temp.clear();
    }
}
int highest_vector(vector<int> &arr1,vector<int> &arr2)
{
    if(arr1.size()>arr2.size())
        return 1;
    if(arr1.size()<arr2.size())
        return -1;
    int i=0;
    for(;i<arr1.size()&&i<arr2.size();i++)
    {
        if(arr1[i]>arr2[i])
            return 1;
        if(arr1[i]<arr2[i])
            return -1;
    }
    if(arr1.size()>i)
        return 1;
    if(arr2.size()>i)
        return -1;
    return 0;
}
void vector_subtraction(vector<int> v1,vector<int> v2,vector<int>&ans)
{
    int flag=highest_vector(v1,v2);
    if(flag==0)
    {
      return;
    }
    if(flag==1)
{


        ans.resize(v1.size());
        copy(v1.begin(),v1.end(),ans.begin());
}
if(flag==-1)
{
    ans.resize(v2.size());
    copy(v2.begin(),v2.end(),ans.begin());
    v2.clear();
    v2.resize(v1.size());
    copy(v1.begin(),v1.end(),v2.begin());
}
        for(vector<int>::reverse_iterator v2it=v2.rbegin(),ansit=ans.rbegin();v2it!=v2.rend();v2it++,ansit++)
{

            if(*ansit>=*v2it)
            {
                *ansit=*ansit-*v2it;
                continue;
            }
            else{
                    int flag=0;
                    vector<int>::reverse_iterator ansit_temp=ansit+1,v2it_temp=v2it+1;
                    //cout<<*ansit_temp<<"h"<<endl;
                for(;v2it_temp!=v2.rend();ansit_temp++,v2it_temp++)
                {
                    if(*ansit_temp>*v2it_temp)
                    {
                        *ansit=*ansit+10-*v2it;
                        (*ansit_temp)--;
                        flag=1;
                        break;
                    }
                    else{

                        *ansit_temp=*ansit_temp+9;

                    }
                }
                if(flag==0)
                {
                    for(;*ansit_temp==0&&ansit_temp!=ans.rend();ansit_temp++)
                    {
                        *ansit_temp=9+*ansit_temp;
                    }
                    (*ansit_temp)--;

                    *ansit=*ansit+10-*v2it;
                }

            }
        }
        vector<int>::iterator it=ans.begin();
        if(*it!=0)
            return;
        else{
            for(;it!=ans.end()&&*it==0;it++);
            vector<int> v3(ans.end()-it);
            copy(it,ans.end(),v3.begin());
            ans.clear();
            ans.resize(v3.size());
            copy(v3.begin(),v3.end(),ans.begin());
        }


}

int main()
{
    ifstream infile("a.txt");
    ofstream outfile("oa1.txt");
    int T;
    infile>>T;
    long long int r,t,num;
    vector<int> vr,vt,rtemp,squ;
    vector<int>add;
    vector <int>squtemp,ttemp,tused;
    add.push_back(1);
    for(int case1=1;case1<=T;case1++)
    {
        outfile<<"Case #"<<case1<<": ";
      infile>>r>>t;

      num=0;
      number_to_vector(r,vr);
      number_to_vector(t,vt);
      vector_multiplication(vr,vr,squ);
      add_vector(vr,add,rtemp);
      vector_multiplication(rtemp,rtemp,squtemp);


          vector_subtraction(squtemp,squ,tused);

      while(highest_vector(vt,tused)>=0)
      {

         num++;
 vr.clear();
 vr.resize(rtemp.size());
 copy(rtemp.begin(),rtemp.end(),vr.begin());
 add_vector(vr,add,vr);
 add_vector(vr,add,rtemp);
 squ.clear();
 vector_multiplication(vr,vr,squ);
 squtemp.clear();
 vector_multiplication(rtemp,rtemp,squtemp);
 vector_subtraction(squtemp,squ,ttemp);
 add_vector(ttemp,tused,tused);
 ttemp.clear();

      }
outfile<<num<<endl;
vr.clear();
rtemp.clear();
squ.clear();
squtemp.clear();
vt.clear();
tused.clear();


    }

}

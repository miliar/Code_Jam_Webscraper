#include<set>
#include<iostream>
#include<cstdlib>
#include<cstdio>
using namespace std;
int main()
{
    int t,n,x,y,d,p,i,ans,c=1,max,ans1=0,omax;
    FILE *fp,*fo;
    fp=fopen("B-small-attempt3.in","r");
    fo=fopen("output.txt","w");
    fscanf(fp,"%d",&t);
    while(t--)
    {
    	max=0;
        ans=0;
        ans1=0;
        omax=0;
        multiset <int> ms,ms1;
        fscanf(fp,"%d",&d);
        for(i=0;i<d;i++)
        {
            fscanf(fp,"%d",&x);
            ms.insert(x);
            ms1.insert(x);
            if(x>max)
            max=x;
        }
        omax=max;
        multiset <int> ::iterator it;
        it=ms.end();
        it--;
        while(1)
        {
        	if(ans+(*it)<max)
        	max=ans+(*it);
            if((*it)==1 || (*it)==2 || (*it)==3)
            {

                ans=ans+(*it);
                if(ans>max)
            {
            	ans=max;
            	break;
            }
                break;
            }
            if((*it)==4)
            {
            	ans++;
            	y=(*it);
                ms.erase(it);
                ms.insert(y/2);
                ms.insert(y/2);
            }
            else
            {
                ans++;
                y=(*it);
                ms.erase(it);
                ms.insert(3);
                ms.insert(y-3);
            }
            if(ans>max)
            {
            	ans=max;
            	break;
            }
            it=ms.end();
            it--;

        }
        //multiset <int> ::iterator it;
        it=ms1.end();
        it--;
        while(1)
        {
        	if(ans1+(*it)<omax)
        	omax=ans1+(*it);
            if((*it)==1 || (*it)==2 || (*it)==3)
            {

                ans1=ans1+(*it);
                if(ans1>omax)
            {
            	ans1=omax;
            	break;
            }
                break;
            }
            if((*it)%2==0)
            {
            	ans1++;
            	y=(*it);
                ms1.erase(it);
                ms1.insert(y/2);
                ms1.insert(y/2);
            }
            else
            {
                ans1++;
                y=(*it);
                ms1.erase(it);
                ms1.insert(y/2);
                ms1.insert(y/2+1);
            }
            if(ans1>omax)
            {
            	ans1=omax;
            	break;
            }
            it=ms1.end();
            it--;

        }
        if(ans>ans1)
        ans=ans1;
        fprintf(fo,"Case #%d: %d\n",c++,ans);

    }
    return 0;
}

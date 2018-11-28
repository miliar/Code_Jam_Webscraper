#include <iostream>

using namespace std;

int main()
{
    int T, testcase=1;
    int N,i,j,k;
    double value;
    cin >> T;
    do
    {
        cin >> N;
        double naomi[N],ken[N];
        double warken[N],cwarken[N];
        for(i=0;i<N;i++)
        {
            cin>>value;
            for(j=i-1;j>=0;j--)
            {
                if(naomi[j]<=value)
                    break;
            }
            for(k=i-1;k>j;k--)
            {
                naomi[k+1]= naomi[k];
            }
            naomi[j+1] = value;
        }
        /*for(i=0;i<N;i++)
            cout<<naomi[i]<<" ";
        cout<<endl;*/
        for(i=0;i<N;i++)
        {
            cin>>value;
            for(j=i-1;j>=0;j--)
            {
                if(ken[j]<=value)
                    break;
            }
            for(k=i-1;k>j;k--)
            {
                ken[k+1]= ken[k];
            }
            ken[j+1] = value;
        }
        /*for(i=0;i<N;i++)
            cout<<ken[i]<<" ";
        cout<<endl;*/
        for(i=0;i<N;i++)
            {
                warken[i]=ken[i];
                cwarken[i]=ken[i];
            }

       //WAR
       int Nken=N;
       int kenwarscore=0;
       int naomiwarscore=0;
       for(i=0;i<N;i++)
       {
           bool found = false;
           for(j=0;j<Nken;j++)
           {
                   if(warken[j]>naomi[i])
                   {
                       found = true;
                       for(k=j;k<Nken-1;k++)
                       {
                           warken[k]=warken[k+1];
                       }
                       Nken--;
                       kenwarscore++;
                       break;
                   }
           }
           if(!found)
           {
               for(k=0;k<Nken-1;k++)
               {
                   warken[k]=warken[k+1];
               }
               Nken--;
               naomiwarscore++;
           }
       }
       //cout<<naomiscore<<" "<<kenscore<<endl;

       //DeceitfulWar
       Nken=N;
       int kencwarscore=0;
       int naomicwarscore=0;
       for(i=0;i<N;i++)
       {
           if(cwarken[0]>naomi[i])
           {
               Nken--;
               kencwarscore++;
           }
           else
           {
               for(k=0;k<Nken-1;k++)
               {
                   cwarken[k]=cwarken[k+1];
               }
               Nken--;
               naomicwarscore++;

           }
       }
       cout <<"Case #"<<testcase<<": ";
       cout<<naomicwarscore<<" "<<naomiwarscore<<endl;

    testcase++;
    }while(testcase<=T);

    return 0;
}

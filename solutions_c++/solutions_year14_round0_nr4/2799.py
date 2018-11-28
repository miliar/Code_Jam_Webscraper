#include<stdio.h>
#include<iostream>
#include<math.h>
#include<algorithm>

using namespace std;

float n[1000] ;
float k[1000];
void input(int data_no)
{
    int i,j;
    for(i=0;i<data_no;i++)
    {
        //scanf("%f",&ff);
       // cout<<"enter " ;
        //cin>>ff;
        cin>>n[i];
        //cout<<n[i]<<" ";
    }
    //cout<<endl;

    for (j=0;j<data_no;j++)
    {
        //cout<<"enter2 " ;
        //scanf("%f",&k[j]);
        cin>>k[j];
        //cout<<k[j]<<" ";
    }



}

int war(float n[1000],float k[1000],int data_no)
{
    int i=0,j=0;
    int count=0;
    for (i=0;i<data_no;)
    {
        for ( ;j<data_no;j++)
        {
            if(n[i]<k[j])
            {
                count++;
                //k[j]=0;
                j++;
                goto aa;
                //continue;
            }
        }
        aa:
            i++;
    }
    return count;
}

int d_war(float n[1000],float k[1000],int data_no)
{
    int i=0,j=0;
    int d_count=0;
    j=data_no-1;
    for (i=data_no-1;i>=0;)
    {
        for ( ;j>=0;j--)
        {
            if(n[i]>k[j])
            {
                d_count++;
                //k[j]=0;
                j--;
                goto aa;
                //continue;
            }
        }
        aa:
            i--;
    }
    return d_count;
}


int main()
{
    int test,data_no;
    int case_no=0;
   // float ff;
    int war_count,d_war_count;
    freopen("d.txt","r",stdin);
    freopen("d_out.txt","w",stdout);
    //scanf("%d",&test);
    cin>>test;
   // printf("%f\n",nn);
    //cout<<test<<endl;

    while(case_no < test)
    {
        case_no++;
        //scanf("%d",&data_no);
        cin>>data_no;
        input(data_no);
        //cout<<data_no<<" \n";
        //input(data_no);
        int i,j;
        //cout<<data;

                //cout<<endl;
        //cout<<endl;
        //n=sort(n,data_no);
        //selectionSort(n,data_no);
        //selectionSort(k,data_no);
        sort(n,n+data_no);
        sort(k,k+data_no);

        /*for (j=0;j<data_no;j++)
        {
            //cout<<"enter2 " ;
            //scanf("%f",&k[j]);
            cout<<n[j]<<" \t";
            //cout<<k[j]<<" ";
        }
        cout<<endl;
        for (j=0;j<data_no;j++)
        {
            //cout<<"enter2 " ;
            //scanf("%f",&k[j]);
            cout<<k[j]<<" \t";
            //cout<<k[j]<<" ";
        }
        cout<<endl<<endl;*/
        // for deceitful war


        d_war_count=d_war(n,k,data_no);
        war_count=war(n,k,data_no);
        war_count=data_no - war_count;

        cout<<"Case #"<<case_no<<": "<<d_war_count<<" "<<war_count<<endl;

    }


}

#include<iostream>
#include<fstream>
using namespace std;
main()
{
	ofstream outputfile("out.txt");
    int n,a[4][4],r1,i,s1[4],s2[4],j,flag,ans;
    cin>>n;
    int iter;
    for(iter=0;iter<n;iter++)
    {
        flag=0;
        cin>>r1;
        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        cin>>a[i][j];

        for(i=0;i<4;i++)
           s1[i]=a[r1-1][i];

        cin>>r1;
        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        cin>>a[i][j];

        for(i=0;i<4;i++)
        {
            s2[i]=a[r1-1][i];
        }
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                {
                    if(s1[i]==s2[j])
                    {
                        flag++;
                        ans=s1[i];
                    }
                }
        }

        if(flag==0)
        {
        	outputfile<<"Case #"<<iter+1<<": Volunteer cheated!\n";
        }
        if(flag==1)
        {
        	outputfile<<"Case #"<<iter+1<<": "<<ans<<endl;
        }
        if(flag>1)
        {
        	outputfile<<"Case #"<<iter+1<<": Bad magician!\n";
        }
    }
    return 0;
}


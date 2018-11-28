#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    int T,i,j,ds1,ds2,d1,d2;
    int s1[4][4],s2[4][4];
    ifstream f1;
	f1.open("F:\\TC\\BIN\\Code_Jam_2\\IS1.in");
	ofstream f2;
	f2.open("F:\\TC\\BIN\\Code_Jam_2\\OS1.out");
	f1>>T;
	int k=1;
	while(T>0)
    {
        f1>>d1;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                f1>>s1[i][j];
        }
        f1>>d2;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                f1>>s2[i][j];
        }
        
        d1--;
        d2--;
        ds1=0;
        ds2=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(ds1==2)
                    break;
                if(s2[d2][j]!=0)
                {
                    if(s1[d1][i]==s2[d2][j])
                    {
                        ds1++;
                        ds2=i;
                        s2[d2][j]=0;
                    }
                }
            }
        }
        if(k!=1)
            f2<<"\n";
        if(ds1==1)
            f2<<"Case #"<<k<<": "<<s1[d1][ds2];
        else if(ds1==0)
            f2<<"Case #"<<k<<": Volunteer cheated!";
        else
            f2<<"Case #"<<k<<": Bad magician!";
        k++;
        T--;
    }
    f1.close();
	f2.close();
	cout<<"DONE!";
	cin>>T;
	return 0;	
}

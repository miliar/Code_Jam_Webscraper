#include<bits/stdc++.h>
#include<fstream>
using namespace std;

int main()
{
    ofstream myfile ;
    myfile.open("GCJ-5.txt") ;
    int t;
    cin >> t;
   int k=1;
    while(t--)
    {

      long int d,max1=0,mintime,current,temp;

      long int p[1010]={0};

      cin >> d;

      for(long int i=1;i<=d;i++)
      {
          cin>>p[i];
          if(p[i]>max1)
            max1=p[i];
      }

    mintime=max1;
     for(long int i=1;i<=max1;i++)
		{
			current=0,temp=0;
			for(long int j=1;j<=d;j++)
			{
				if(p[j]>i)
				{
					current += (p[j]/i)-1;

					if(p[j]%i!=0)
                    current+=1;

					if(i>temp)
                     temp=i;
				}
				else
                {
                    if(p[j]>temp)
                     temp=p[j];
                }
			}

			current+=temp;
			if(current<mintime)
             mintime=current;
		}

  myfile << "Case #" << k << ": " << mintime << endl;
     k++;

    }

    return 0;
}

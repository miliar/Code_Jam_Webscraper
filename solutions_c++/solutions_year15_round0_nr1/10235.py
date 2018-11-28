#include <iostream>


#include<fstream>

using namespace std;

int main()

{


	char s[100];

	int ne[100],i,re[100];

	int smax,no,count,count1,t;

	cin>>t;

	for(int j=0;j<t;j++)

	{

		cin>>smax;
	
	int max=smax+1;
	
	for(i=0;i<max;i++)

			cin>>s[i];

		for(i=0;i<=smax;i++)

		{

			switch(s[i])
		{
            case 49:

                ne[i]=1;
                break;
  
            case 50:

                ne[i]=2;
                break;
  
            case 51:
  
                ne[i]=3;
                break;

            case 52:

                ne[i]=4;
                break;
  
            case 53:

                ne[i]=5;
                break;
  
            case 54:

                ne[i]=6;
                break;

            case 55:

                ne[i]=7;
                break;

            case 56:
  
                ne[i]=8;
                break;
  
            case 57:

                ne[i]=9;
                break;
  
            case 48:

                ne[i]=0;
                break;
		}

		}
		if(smax>0)
	
	{

			no=ne[0];

			count=0;

			for(i=1;i<=smax;i++)

			{

				if(i<=no)

				{
	
					no=no+ne[i];

				}

				else

				{

					if(s[i]==0)

						continue;

					count1=i-no;

					count+=count1;

					no=no+count1;
	
				no=no+ne[i];
	
			}


			}
	
		re[j]=count;
	
	
}

		else
	
	    re[j]=0;

	}

	ofstream Myfile;
	Myfile.open("output.txt");
	for(i=0;i<t;i++)
	{

	    Myfile<<"Case #"<<i+1<<": "<<re[i]<<endl;

	}

	Myfile.close();
	return 0;

}


//Counting Sheep
#include<iostream.h>
#include<fstream.h>
#include<conio.h>

int main()
{
	ifstream in;
        ofstream out;
        in.open("input1_s.txt");
        out.open("output_s.txt");

        int cases;
        in>>cases;

        int i;
        long int num;

        clrscr();

        for(i=1;i<=cases;i++)
        {

        	in>>num;
                if(num==0)
                	out<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
                else
                {
                	int flag=0,mul_factor=1,j,sum,dig;
                        long int temp,num1=num;

                	int count[10];
                	for(j=0;j<=9;j++)
                		count[j]=-1;

                	while(flag==0)
                	{
                		temp=num1;

                        	while(temp>0)
                        	{
                        		dig=temp%10;
                                	count[dig]=1;
                                	temp=temp/10;
                        	}

                        	sum=0;
                        	for(j=0;j<=9;j++)
                        		sum=sum+count[j];

                        	if(sum==10)
                        	{
                        		out<<"Case #"<<i<<": "<<num1<<endl;
                        		flag=1;
                        	}
                        	else
                        	{
                        		mul_factor++;
                                	num1=num*mul_factor;
                        	}

                	}

        	}
        }
        in.close();
        out.close();
        getch();
        return 0;

}


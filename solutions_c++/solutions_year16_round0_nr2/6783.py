//Revenge of the pancakes
#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<string.h>

int main()
{
	ifstream in;
        ofstream out;
        in.open("input2_s.txt");
        out.open("output2.txt");
 	clrscr();

        int cases;
        in>>cases;

        char c;
        int i;
        char input[100];
        for(i=1;i<=cases;i++)
        {
        	in>>input;
                int j;
                int count=1;
                char array[100];
                j=0;
                while(j<strlen(input))
                {
                	if(input[j]=='+')
                        {
                        	while(input[j]!='-'&&j<strlen(input))
                                	j++;
                                array[count]='+';
                                count++;
                        }
                        if(input[j]=='-')
                        {
                        	while(input[j]!='+'&&j<strlen(input))
                                	j++;
                                array[count]='-';
                                count++;
                        }


                }
                count--;
                if(array[1]=='+')
                {
                	if(array[count]=='+')
                        	out<<"Case #"<<i<<": "<<count-1<<endl;
                        else if(array[count]=='-')
                        	out<<"Case #"<<i<<": "<<count<<endl;
        	}
                else if(array[1]=='-')
                {
                	if(array[count]=='-')
                        	out<<"Case #"<<i<<": "<<count<<endl;
                        else if(array[count]=='+')
                        	out<<"Case #"<<i<<": "<<count-1<<endl;
                }
        }
	getch();
        return 0;
}
#include<iostream>
#include<string.h>

using namespace std;

int main()
{
    char cakestack[101], cases[4], c;
    int no_of_manouvers = 0, stack_size = 0, T;
    int i, j, k, iter = 0;

    //T = atoi(fgets(cases, 4, stdin));
    cin>>T;
    for(i = 0; i < T; i++)
    {
	no_of_manouvers = 0;
	//fgets(cakestack, 101, stdin);
	cin >> cakestack;
	stack_size = strlen(cakestack);
	if(cakestack[stack_size - 1] == '\n')
	    stack_size--;
	if(stack_size == 0)
	    continue;
	else iter++;
	cout<<"Case #"<<iter<<": ";
	do
	{
	    j = 0;
	    while(j < stack_size && cakestack[j] != '-')
		j++;
	    if(j == stack_size)
	    {
		cout<<no_of_manouvers<<endl;
		break;
	    }
	    else
	    {
		while(j < stack_size && cakestack[j] != '+')
		    j++;
		for(k = 0; k < j; k++)
		{
		    if(cakestack[k] == '-')
			cakestack[k] = '+';
		    else
			cakestack[k] = '-';
		}
		no_of_manouvers++;
	    }
	}while(1);
    }
}



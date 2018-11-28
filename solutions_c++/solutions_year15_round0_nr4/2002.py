#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int i=0;
	while(i<t)
	{
		int a,b,c;
		cin>>a>>b>>c;
		cout<<"Case #"<<i+1<<": ";
		switch(a)
		{
			case 1:
				printf("GABRIEL\n");
                               	break;
			case 2:
				switch(b%2+c%2)
				{
					case 0:
					case 1:
						printf("GABRIEL\n");
						break;
					case 2:
						printf("RICHARD\n");
                                                break;
				}
                                break;
			case 3:
				switch(b)
				{
					case 2:
						switch(c)
						{
							case 3:
								printf("GABRIEL\n");
	                                                	break;
							default:
								printf("RICHARD\n");
						}
						break;
					case 3:
						switch(c)
						{
							case 1:
								printf("RICHARD\n");
                                                		break;
							default:
								printf("GABRIEL\n");
						}
						break;
					case 4:
						switch(c)
						{
							case 3:
								printf("GABRIEL\n");
		                                                break;
							default:
								printf("RICHARD\n");
						}
						break;
					default:
						printf("RICHARD\n");
				}
                                break;
			case 4:
				switch(b)
				{
					case 3:
						switch(c)
						{
							case 4:
								printf("GABRIEL\n");
		                                                break;
							default:
								printf("RICHARD\n");
						}
						break;
					case 4:
						switch(c)
						{
							case 3:
							case 4:
								printf("GABRIEL\n");
	                                                	break;
							default:
								printf("RICHARD\n");
						}
						break;
					default:
						printf("RICHARD\n");
				}
		}
		i++;
	}
	return 0;

}


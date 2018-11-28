#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int t, n, cuenta, coef=1,cont,temp;
string num;
bool num0,num1,num2,num3,num4,num5,num6,num7,num8,num9;

int main()
{
	cin.tie(0);
	cin.sync_with_stdio(0);
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>n;
		if(n==0)
		{
			cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
		}
		else
		{
			coef=1;
			temp=0;
			cuenta=0;
			num0=num1=num2=num3=num4=num5=num6=num7=num8=num9=false;
			while(cuenta!=10)
			{
				temp=coef*n;
				stringstream ss;
				ss<<temp;
				num=ss.str();
				while(cont<num.size())
				{
					if(num[cont]=='0' && !num0)
					{
						cuenta++;
						num0=true;
					}
					else if(num[cont]=='1' && !num1)
					{
						cuenta++;
						num1=true;
					}
					else if(num[cont]=='2' && !num2)
					{
						cuenta++;
						num2=true;
					}
					else if(num[cont]=='3' && !num3)
					{
						cuenta++;
						num3=true;
					}
					else if(num[cont]=='4' && !num4)
					{
						cuenta++;
						num4=true;
					}
					else if(num[cont]=='5' && !num5)
					{
						cuenta++;
						num5=true;
					}
					else if(num[cont]=='6' && !num6)
					{
						cuenta++;
						num6=true;
					}
					else if(num[cont]=='7' && !num7)
					{
						cuenta++;
						num7=true;
					}
					else if(num[cont]=='8' && !num8)
					{
						cuenta++;
						num8=true;
					}
					else if(num[cont]=='9' && !num9)
					{
						cuenta++;
						num9=true;
					}
					cont++;
				}
				coef++;
				cont=0;
				num.clear();
			}
			cout << "Case #" << i+1 << ": " << temp << endl;
		}
	}
	return 0;
}
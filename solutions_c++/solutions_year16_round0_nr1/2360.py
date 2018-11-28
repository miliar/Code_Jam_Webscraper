#include<iostream>
#include<string>

int main()
{
	char arr[10];
        
	int T;
	int N;
        std::cin>>T;
        for(int i=0;i<T;i++)
	{
		std::cin>>N;
		int q=2;
		for(int j=0;j<10;j++)
			arr[j]=0;
		int tmp = N;
		while (true)
		{
			std::string s = std::to_string(N);
			for(int k=0;k<s.length();k++)
			{
				arr[s[k]-'0'] = 1;
			}
			int fin = 1;
			for(int j=0;j<10;j++)
			{
				if (arr[j] == 0)
					fin = 0;
			}			
			if (fin)
				break;
			
			N = tmp*q;
			q++;
			if (N==tmp)
			{
				break;			
			}
		}
		std::cout << "Case #" << i+1 << ": " << (N == 0 ? "INSOMNIA" : std::to_string(N)) << std::endl;	
	}
}

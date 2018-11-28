#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
using namespace std;


int toBina(int x, int RE)
{
	switch(x)
	{
	case 1:
		RE = RE | 0x01;
		break;
	case 2:
		RE = RE | 0x02;
		break;
	case 3:
		RE = RE | 0x04;
		break;
	case 4:
		RE = RE | 0x08;
		break;
	case 5:
		RE = RE | 0x10;
		break;
	case 6:
		RE = RE | 0x20;
		break;
	case 7:
		RE = RE | 0x40;
		break;
	case 8:
		RE = RE | 0x80;
		break;
	case 9:
		RE = RE | 0x100;
		break;
	case 10:
		RE = RE | 0x200;
		break;
	case 11:
		RE = RE | 0x400;
		break;
	case 12:
		RE = RE | 0x800;
		break;
	case 13:
		RE = RE | 0x1000;
		break;
	case 14:
		RE = RE | 0x2000;
		break;
	case 15:
		RE = RE | 0x4000;
		break;
	case 16:
		RE = RE | 0x8000;
		break;
	default:
		break;
	}
	return RE;
}

int main()
{
	string everyline, word;
	ifstream DATA("A-small-attempt7.in");//用户数据
	freopen("output.in","w",stdout);
	int CaseNum = 0; //测试数据的数量
	int Ans = 0;
	int firRE, secRE;
	getline(DATA, everyline);
	if(CaseNum == 0)
	{
		CaseNum= atoi(everyline.c_str());  
	}
	for(int idata = 0; idata < CaseNum; ++idata)
	{
		//THIS IS WHERE WE START>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
		if(idata ==44)
		{
			Ans =0;
		}
		
		firRE=0;
		secRE =0;
		Ans =0;
		int count =0;
		int answer =0;
		int FirAns = 0, SecAns =0;
		if(!getline(DATA, everyline))
		{
			//cout<<"error"<<endl;
			DATA.close();
			return 0;
		}
		//cout<<everyline<<endl;
		if(FirAns == 0)
		{
			FirAns= atoi(everyline.c_str());  
		}
		for(int i = 1; i<=4; ++i)
		{
			if(!getline(DATA, everyline))
			{
			//cout<<"error"<<endl;
				DATA.close();
			return 0;
			}
		//	cout<<everyline<<endl;
			if( FirAns== i )
			{
				istringstream strea(everyline);
				for( int c = 0; c<4; ++c)
				{
					if(strea >> word)
					{
						
						firRE = toBina(atoi(word.c_str()), firRE);
						
					}
				}
				strea.clear();
			}
		}
		if(!getline(DATA, everyline))
		{
		//	cout<<"error"<<endl;
			DATA.close();
			return 0;
		}
		if(SecAns == 0)
		{
			SecAns= atoi(everyline.c_str());  
		//	cout<<SecAns<<endl;
		}
		
		for(int j = 1; j<=4; ++j)
		{
			if(!getline(DATA, everyline))
			{
				//cout<<"error"<<endl;
				DATA.close();
				return 0;
			}
		//	cout<<everyline<<endl;
			if( j== SecAns)
			{
				istringstream strea(everyline);
				for( int c = 0; c<4; ++c)
				{
					if(strea >> word)
					{
						
						secRE = toBina(atoi(word.c_str()), secRE);
					}
				}
				strea.clear();
			}
		}
	
		//JUDGE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
		
		
			Ans = firRE & secRE;
		//	cout<<hex<< firRE  <<" "<<secRE <<" "<<Ans<<dec<<endl;

			for(int i=1;i<=16;i++)
			{
				if(Ans%2)
				{
					answer = i;
					count++;
				}
				Ans = Ans/2;
			}
		
		
		if(count==1)
		{
			cout<< "Case #"<< idata+1 <<": "<<answer<<endl;
		}
		else if(count>1)
		{
			cout<< "Case #"<< idata+1 <<": Bad magician!"<<endl;
		}
		else if(count ==0)
		{
			cout<< "Case #"<< idata+1 <<": Volunteer cheated!"<<endl;
		}

	}
	DATA.close();
	//system("PAUSE");
	return 0;
}
#include <iostream>
#include <cstring>
using namespace std;

int map[256];
char negMap[256];
bool isNegMap[256];

int matrix[4][4] =
{
	{'1','i','j','k'},
	{'i','2','k','y'},
	{'j','z','2','i'},
	{'k','j','x','2'},
};

//{
//	{'1','i','j','k'},
//	{'i','-1','k','-j'},
//	{'j','-k','-1','i'},
//	{'k','j','-i','-1'},
//};

char mul(char a, char b)
{
	//cout<<"mul("<<a<<","<<b<<")"<<endl;
	return matrix[map[a]][map[b]];
}

char toPositive(char c, bool *isNeg)
{
	//cout<<"toPositive("<<c<<","<<*isNeg<<")"<<endl;
	(*isNeg) = (*isNeg) ^ isNegMap[c];
	//cout<<"isNeg="<<(*isNeg)<<endl;
	if(isNegMap[c])
	{
		return negMap[c];
	}
	return c;
}

static char s[10000000000000LL];

int main()
{
	map['1']=0; map['i']=1; map['j']=2; map['k']=3;
	isNegMap['2']=isNegMap['x']=isNegMap['y']=isNegMap['z']=true;
	negMap['2']='1'; negMap['x']='i'; negMap['y']='j'; negMap['z']='k';

	char a,b;
	bool neg;
		
	long long t = 0;
	cin>>t;
	
	long long l,x;
	for(long long ti = 0; ti < t; ti++)
	{
		cin>>l>>x;
		cin>>s;
	
		neg = false;	
		char res = s[0];
		
		bool ca=false,cb=false,cc=false;
		
		if(res=='i'){if(!ca)ca=true;}
		else if(res=='j'){if(!cb)cb=true;}
		else if(res=='k'){if(!cc)cc=true;}
		
		long long m = l*x;
		int finding = 0;
		for(long long  j = 1; j < m; j++)
		{
			long long i = j % l;
			char ch = s[i];
			
			//cout<<"finding="<<finding<<" ";
			
			bool found = false;
			if(finding==0){if(res=='i') found = true;}
			else if(finding==1){if(res=='j') found = true;}
			else if(finding==2){if(res=='k') found = true;}
			
			//cout<<"finding="<<finding<<" ";
			
			if(found) {
				//cout<<"found="<<res;
				finding++;
				res = ch;
				
				if(j==m-1) {
					//cout<<"*";
					if(finding==0){if(res=='i') finding++;}
					else if(finding==1){if(res=='j') finding++;}
					else if(finding==2){if(res=='k') finding++;}
					
				}
				//cout<<endl;
				continue;
			}
			
			if(ch=='i'){if(!ca)ca=true;}
			else if(ch=='j'){if(!cb)cb=true;}
			else if(ch=='k'){if(!cc)cc=true;}
			res = mul(res,ch);
			//cout<<"res="<<res<<endl;
			res = toPositive(res,&neg);
			
			//cout<<"res="<<res<<endl<<endl;
		}
		//cout<<"neg="<<neg<<" "<<"res="<<res<<endl;
//		bool lastNeg = neg;
//		neg = false;
//		
//		for(int i = 1; i < x; i++)
//		{
//			res = mul(res,res);
//			//cout<<"res="<<res<<endl;
//			res = toPositive(res,&neg);
//			//cout<<"res="<<res<<endl<<endl;
//			
//		}
		//cout<<"neg="<<neg<<" "<<"res="<<res<<endl;
//		cout<<"last="<<lastNeg<<" neg="<<neg<<" res="<<res<<endl;
		bool yes = false;
//		cout<<l<<" "<<x<<" "<<res<<" "<<ca<<" "<<cb<<" "<<cc<<endl;
		if(strcmp(s,"ijk") == 0 && x % 2 == 1) yes = true;
		else if(finding==3 && res=='1' && !neg) yes=true;
//		else if	(x*l > 3 && res=='1' &&((ca&&cb) || (ca&&cc) || (cb&&cc)))
//		{
//			
//			yes = neg;
////			if((!lastNeg && (neg)) || (lastNeg && x%2 == 1 && !neg) || (lastNeg && x%2 == 0 && neg))
////			{
////				yes = true;
////			}
//		}
		//(x*l > 3 && ((res=='1' && neg) || !(neg ^ ((x%2) == 0))));
		
		
		
		cout<<"Case #"<<(ti+1)<<": "<<(yes ? "Yes" : "No")<<endl;
	}
	return 0;	
}

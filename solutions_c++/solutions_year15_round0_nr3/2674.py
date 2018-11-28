/*
ID: k.kamal1
PROG: test
LANG: C++     
*/
#include <bits/stdc++.h>

using namespace std;

/*int main() {
    ofstream fout ("o.out");
    ifstream fin ("in.in");
    int tetC;
    fin >> tetC;
    for(int cnt = 0; cnt < tetC; cnt++)
    {
    	int num;
    	fin >> num;
    	int mx = -1;
		for(int ct = 0; ct < num; ct++)
    	{
    		int cur;
    		fin >> cur;
    		mx = max(mx , cur);
    	}
    	cout << mx << endl;
    	int ret = 1;
    	int cur = 1;
    	while(cur < mx)
    	{
    		ret++;
    		cur*=2;
    	}
    	
    	fout << "Case #" << cnt+1 << ": " << ret << endl; 
     }
    return 0;
}


vector<int> vec;


void prn(vector<int>& vc)
{
	for(int ct =0; ct < vc.size(); ct++)
	{
		cout << " " << vc[ct];
	}
	cout << endl;
}

int get(vector<int>& vc)
{
	//prn(vc);
	int mxv =  *max_element(vc.begin(), vc.end());
	if(mxv == 1)
	return 1;
	
	for(int ct = 0; ct < vc.size(); ct++)
	{
		vc[ct]--;
	}
	int t5 = get(vc);
	
	for(int ct = 0; ct < vc.size(); ct++)
	{
		vc[ct]++;
	}
	
	vc.erase(max_element(vc.begin(), vc.end()));
	if(mxv % 2 == 0)
	{
		vc.push_back(mxv/2);
	}
	else
	{
		vc.push_back((mxv/2) + 1);
	}	
	vc.push_back(mxv/2);
	int t7 = get(vc);
	
	if(mxv % 2 == 0)
	{
		vc.erase(find(vc.begin(), vc.end() , mxv/2));
	}
	else
	{
		vc.erase(find(vc.begin(), vc.end() , (mxv/2) + 1));
	}
	vc.erase(find(vc.begin(), vc.end() , mxv/2));
	
	vc.push_back(mxv);
	
	
	int retV =  t5 < t7 ? t5 + 1: t7 +1;
	return retV;
	
}


int main() {
    ofstream fout ("o.out");
    ifstream fin ("in.in");
    int tetC;
    fin >> tetC;
    for(int cnt = 0; cnt < tetC; cnt++)
    {
    	int num;
    	fin >> num;
    	vec.clear();
		cout << " ererte " << endl;
		for(int ct = 0; ct < num; ct++)
    	{
    		int cur;
    		fin >> cur;
    		vec.push_back(cur);
    	}
    	int ret = get(vec);
    	
    	
    	fout << "Case #" << cnt+1 << ": " << ret << endl; 
     }
    return 0;
}








int main() {
    ofstream fout ("o.out");
    ifstream fin ("in.in");
    int tetC;
    fin >> tetC;
    for(int cnt = 0; cnt < tetC; cnt++)
    {
    	int xt,rw,cl;
    	fin >> xt>>rw>>cl;
    	int ret = 0;
    	if(xt == 2)
    	{
    		if( (rw * cl) % 2 != 0)
    		ret = 1;
    		if((rw * cl) < 2)
    		ret = 1;
    	}
    	else if(xt == 3)
    	{
    		if( (rw * cl) % 3 != 0)
    		ret = 1;
    		if((rw * cl) < 3)
    		ret = 1;
    		
    		if(rw == 1 || cl == 1)
    		ret = 1;
    	}
    	else if(xt == 4)
    	{
    		if( (rw * cl) % 4 != 0)
    		ret = 1;
    		if((rw * cl) < 4)
    		ret = 1;
    		
    		if(rw == 1 || cl == 1)
    		ret = 1;
    		
			if(rw == 2 && cl == 2)
    		ret = 1;
    		if(rw == 2 && cl == 4)
    		ret = 1;
    		if(rw == 4 && cl == 2)
    		ret = 1;
    		
    	}
    	
		
		if(ret == 1)
		fout << "Case #" << cnt+1 << ": RICHARD" << endl;
		else
		fout << "Case #" << cnt+1 << ": GABRIEL" << endl; 
     }
    return 0;
}
*/





char arr[10005];
string cur , tmp;
    

char gt(char c5, char c7, int& rv)
{
	if(c5 == '1' && c7 == '1')
	{
		rv = 1;
		return '1';
	}
	else if(c5 == '1' && c7 == 'i')
	{
		rv = 1;
		return 'i';
	} 
	else if(c5 == '1' && c7 == 'j')
	{
		rv = 1;
		return 'j';
	} 
	else if(c5 == '1' && c7 == 'k')
	{
		rv = 1;
		return 'k';
	}
	
	/////////////
	else if(c5 == 'i' && c7 == '1')
	{
		rv = 1;
		return 'i';
	}
	else if(c5 == 'i' && c7 == 'i')
	{
		rv = -1;
		return '1';
	} 
	else if(c5 == 'i' && c7 == 'j')
	{
		rv = 1;
		return 'k';
	} 
	else if(c5 == 'i' && c7 == 'k')
	{
		rv = -1;
		return 'j';
	} 
	
	
	////////////////
	else if(c5 == 'j' && c7 == '1')
	{
		rv = 1;
		return 'j';
	}
	else if(c5 == 'j' && c7 == 'i')
	{
		rv = -1;
		return 'k';
	} 
	else if(c5 == 'j' && c7 == 'j')
	{
		rv = -1;
		return '1';
	} 
	else if(c5 == 'j' && c7 == 'k')
	{
		rv = 1;
		return 'i';
	}
	
	
	
	////////////////////////////
	else if(c5 == 'k' && c7 == '1')
	{
		rv = 1;
		return 'k';
	}
	else if(c5 == 'k' && c7 == 'i')
	{
		rv = 1;
		return 'j';
	} 
	else if(c5 == 'k' && c7 == 'j')
	{
		rv = -1;
		return 'i';
	} 
	else if(c5 == 'k' && c7 == 'k')
	{
		rv = -1;
		return '1';
	}
	
	
}

bool cn()
{
	char tot = cur[0];
	int curV = 1;
	for(int ct = 1; ct < cur.size(); ct++)
	{
		int tmv;
		tot = gt(tot , cur[ct] , tmv);
		if(tmv == -1)
		{
			if(curV == -1)
			curV = 1;
			else
			curV = -1;
		}
	}
	
	if(curV == -1 && tot == '1')
	return true;
	else
	return false;
}



bool on(int fr)
{
	for(int ct = fr; ct < cur.size(); ct++)
	{
		if(cur[ct] != 'i')
		return true;
	}
	
	return false;
}





vector<int> v5,v7;

int main() {
    ofstream fout ("o.out");
    ifstream fin ("in.in");
    int tetC;
    fin >> tetC;
    for(int cnt = 0; cnt < tetC; cnt++)
    {
    	int num, rep;
    	fin >> num >> rep;
    	fin >> cur;
    	tmp = cur;
    	for(int ct = 0; ct < rep-1; ct++)
    	{
    		cur += tmp;
    	}

		bool ret = false;
		if(cur.size()<3 || !cn())
			ret = false;
		else 
		{
			char tot = cur[0];
			int curV = 1;
			bool f3 = false;
			int ct3 = -1;
			bool f5 = false;
			int ct5 = -1;
			
			
			if(tot == 'i')
			{
				if(cur.size() >= 3 && on(1)) 
				{
					f3 = true;
					ct3 = 0;
				}
			}

			else
			{
			
				for(int ct = 1; ct < cur.size(); ct++)
				{
					int tmv;
					tot = gt(tot , cur[ct] , tmv);
					if(tmv == -1)
					{
						if(curV == -1)
						curV = 1;
						else
						curV = -1;
					}
					
					if(curV == 1 && tot == 'i')
					{
						if(cur.size() - 1 - ct >= 2 && on(ct+1)) 
						{
							f3 = true;
							ct3 = ct;
							break;
						}
					}					
					
				}
			}
			if(f3)
			{
				
				char tot = cur[cur.size() - 1];
				int curV = 1;
				if(tot == 'k')
				{
					f5 = true;
					ct5 = cur.size() - 1;
				}
				else
				{
				
					for(int ct = cur.size() - 2; ct > ct3+1; ct--)
					{
						//cout << curV << " " << tot << endl;
						int tmv;
						tot = gt(cur[ct] , tot , tmv);
						if(tmv == -1)
						{
							if(curV == -1)
							curV = 1;
							else
							curV = -1;
						}
						if(curV == 1 && tot == 'k')
						{
							f5 = true;
							ct5 = ct;
							break;
						}
							
					}
				}
				if(f5)
				ret = true;
			}
			
			
			
			
		}
		
		string retVal = "";
		if(ret)
		retVal += "YES";
		else
		retVal += "NO";
    	fout << "Case #" << cnt+1 << ": " << retVal << endl; 
     }
    return 0;
}


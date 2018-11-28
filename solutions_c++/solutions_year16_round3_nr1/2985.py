#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

bool fcn_sort(pair<int, char>  vt1, pair<int, char>  vt2)
{
    return vt1.first > vt2.first;
}

int main()
{
	ifstream inp;
	ofstream out;
	inp.open("input.txt");
	out.open("output.txt");
	char nameParty [26];
	int i,j;
	for (i=0;i<26;i++)
		nameParty [i] = 'A' + i;
	int party[26];
	
	int testcase;
	inp>>testcase;
	int incase=0;
	int sum = 0;
	int N;
	while (incase < testcase)
	{
		incase++;
		vector <int > vt;
		inp>>N;
		sum = 0;
		int tmpArr[26];
		int temp = 0;
		for (i=0;i<N;i++)
		
		{
			inp>>party[i];
			sum+= party[i];
			tmpArr[i] = i;
			vt.push_back(party[i]);
		}
		
		for (i=0;i<N-1;i++)
			for (j=i+1;j<N;j++)
				if (party[i] < party[j])
				{
					temp = party[i];
					party[i] = party[j];
					party[j] = temp;
					temp = tmpArr[i];
					tmpArr[i] = tmpArr[j];
					tmpArr[j] = temp;
					
				}
		
		
		out<<"Case #"<<incase<<": ";
		int p = 0; 
		int c = 0;
		while (vt.size() >0) {
			
			for (i=0;i<N-1;i++)
				for (j=i+1;j<N;j++)
				if (party[i] < party[j])
				{
					temp = party[i];
					party[i] = party[j];
					party[j] = temp;
					temp = tmpArr[i];
					tmpArr[i] = tmpArr[j];
					tmpArr[j] = temp;
					
				}
			if (party[0] == 1 && sum==3)
			{
				party[0]--;
				out<<nameParty[tmpArr[0]];
				sum--;
				vt[0]--;
				vt.erase(vt.begin()+0);
			}
			else
			{
				if (vt.size() >= 2)
				{
					vt[0]--;
					party[0]--;
					party[1]--;
                    out<<nameParty[tmpArr[0]];
                    vt[1]--;
                    out<<nameParty[tmpArr[1]];
                    if (vt[1] == 0) {
                        vt.erase(vt.begin()+1);
                    }
                    if (vt[0] == 0) {
                        vt.erase(vt.begin()+0);
                    }
				}
				
				else
				{
					if (party[0] == 1) {
                        vt[0] --;
                        party[0] --;
                        out<<nameParty[tmpArr[0]];
                        if (vt[0] == 0) {
                            vt.erase(vt.begin()+0);
                        }
                    }
                    else if (party[0] >= 2)
                    {
                        vt[0] = vt[0] - 2;
                        party[0] = party[0] - 2;
                        out<<nameParty[tmpArr[0]]<<nameParty[tmpArr[0]];
                        if (vt[0] == 0) {
                            vt.erase(vt.begin()+0);
                        }
                    }
				}
			}
			
			
		
            out << " ";
        }
        out << endl;
		
		
	}
	
	
	inp.close();
	out.close();
	return 0;
}

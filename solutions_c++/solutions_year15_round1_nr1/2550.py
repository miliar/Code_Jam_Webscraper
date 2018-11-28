#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <map>

using namespace std;



void main()
{
	ifstream in("3.in");
//	streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	cin.rdbuf(in.rdbuf());//redirect std::cin to in.txt!

	ofstream out("3.out");
//    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    cout.rdbuf(out.rdbuf());

	
	int testcases;
	cin>>testcases;
	
	
	for(int i = 0 ; i< testcases ; i++)
	{
		int num;
		priority_queue<int> q;
		cin>>num;
		int * status = new int[num];
		int * difference = new int[num];
		int total = 0;
		int maxdifference = 0;
		for(int j = 0 ; j< num ; j++)
		{
			cin>>status[j];
			difference[j] = (j == 0?0:status[j-1]-status[j]); 
			if(j<=1)
			{
				maxdifference = (difference[j]>0?difference[j]:maxdifference);
			}
			else
				maxdifference = (maxdifference<difference[j] && difference[j]>0)?difference[j]:maxdifference;
			total  = total + (difference[j]>0?difference[j]:0);
		}
		
		int minimumway2 = 0;
		for(int j = 0 ; j< num-1 ; j++)
		{
			if(status[j]>=maxdifference)
				minimumway2 += maxdifference;
			else
				minimumway2+=status[j];
		}
		cout<<"Case #"<<i+1<<": "<<total<<" "<<minimumway2<<endl;


	}
}
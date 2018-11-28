#include <iostream>
#include <vector>
#include <cmath>
#include <list>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

typedef long long ll;

struct chart{
	vector<int> *num;
	string past;
	int time;
};


void vectorCopy( chart *&temp, chart *&copy )
{
	copy->num->clear();
	for( ll i = 0; i < temp->num->size(); i++ )
	{
		copy->num->push_back( temp->num->at(i) );
	}
	copy->time = temp->time;
	copy->past = temp->past;
}

void timetable( chart *&temp )
{
	//chart *temp;
	chart *copy1;
	list<chart *> queue;
	temp -> time = 0;
	temp -> past = "";
	//temp = new chart;
	//temp->num = new vector<int>;
	//temp->time = 0;
	//temp->num->push_back(max);
	queue.push_back(temp);
	//queue.push_back( plates );
	while( !queue.empty() )
	{
		temp = queue.front();
		queue.pop_front();
		//cerr << "Time " << temp -> time << " : ";
		temp -> past += "time ";
		stringstream ss;
		ss << temp -> time;
		temp -> past += ss.str();
		temp -> past += " :";
		for( ll i = 0; i < temp->num->size(); i++ )
		{
			stringstream s2;
			s2 << temp -> num -> at(i);
			temp -> past += s2.str();
			temp -> past += " ";
			//cerr << temp -> num -> at(i) << " ";
		}
		temp -> past += "\n";
		//cerr << endl;
		//cerr << temp -> past << endl;
		bool good = true;
		for( ll i = 0; i < temp->num->size(); i++ )
		{
			if( temp->num->at(i) > 0 )
			{
				good = false;
				break;
			}
		}
		if( good )
		{
			cerr << temp -> past << endl;
			cout << temp-> time << endl;
			break;
		}
		
		
		copy1 = new chart;
		copy1->num = new vector<int>;
		vectorCopy( temp, copy1 );
		int max = 0;
		int secondMax = max;
		int pos = 0;
		for( ll i = 0; i < copy1->num->size(); i++ )
		{
			if( copy1->num->at(i) > max )
			{
				max = copy1->num->at(i);
				pos = i;
			}
			
		}
		for( ll i = 0; i < copy1->num->size(); i++ )
		{
			if( copy1->num->at(i) < max && copy1->num->at(i) > secondMax )
			{
				secondMax = copy1->num->at(i);
			}
			
		}
		if( max == 9 && secondMax <= 3 || max == 9 && secondMax == 6 )
		{
			copy1->num->at(pos) = 6;
			copy1->num->push_back(3);
			copy1->time++;
		}else
		{
			copy1->time++;
			copy1->num->push_back(copy1->num->at(pos) / 2);
			copy1->num->at(pos) -= (copy1->num->at(pos) / 2);
		}
		
		queue.push_back( copy1 );
		
		/*for( ll i = 0; i < temp->num->size();i++  )
		{
			if( copy1->num->at(i) > (temp->num->at(pos) / 2) && copy1->num->at(i)!= 0 )
			{
				copy1 = new chart;
				copy1->num = new vector<int>;
				vectorCopy( temp, copy1 );
				copy1->num->at(i) += (temp->num->at(pos) / 2);
				copy1->num->at(pos) -= (temp->num->at(pos) / 2);
				copy1->time++;
				queue.push_back( copy1 );
			}
		}*/
		
		for( ll i = 0; i < temp->num->size(); i++ )
		{
			if( temp->num->at(i) > 0 )
				temp->num->at(i) = temp->num->at(i) - 1;
		}
		
		temp->time++;
		queue.push_back( temp );
		
		
	}
	//cout << queue.size() << endl;
	for( ll i = 0; i < queue.size(); i++ )
	{
		queue.front() -> num -> clear();
	}
	queue.clear();
}

int main()
{
	int casses;
	cin >> casses;
	chart *temp = new chart;
	int hold;
	temp->num = new vector<int>;
	int nonEmptyPlates;
	for( int i = 0; i < casses && cin >> nonEmptyPlates; i++ )
	{
		temp->num->clear();
		temp->time = 0;
		//cout  << "Hold ";
		for( int j = 0; j < nonEmptyPlates; j++ )
		{
			cin >> hold;
			//cout << hold << " ";
			temp->num->push_back( hold );
		}
		//cout << endl;
		cout << "Case #" << i + 1 << ": ";
		timetable(temp);
		
		
	}
	
	
	/*int casses;
	cin >> casses;
	vector<ll> plates;
	string setUp[1000];
	int nonEmptyPlates;
	int temp;
	int maxStackNum;
	int numOfStacks;
	int past;
	int answer;
	int tempSize1;
	for( int i = 0; i < casses && cin >> nonEmptyPlates; i++ )
	{
		maxStackNum = -1;
		numOfStacks = -1;
		answer = 10000;
		for( int i = 0; i < 1000; i++ )
		{
			setUp[i] = "";
		}
		for( int i = 0; i < nonEmptyPlates; i++ )
		{
			cin >> temp;
			plates.push_back( temp );
		}
		while( true )
		{
			past = maxStackNum;
			for( int i = 0; i < plates.size(); i++ )
			{
				if( plates[i] > past )
				{
					maxStackNum = plates[i];
					break;
				}
			}
			if( past == maxStackNum )
			{
				break;
			}
			numOfStacks = 0;
			for( int i = 0; i < plates.size(); i++ )
			{
				if( plates[i] == maxStackNum )
				{
					numOfStacks++;
				}
			}
			tempSize1 = 0;
			for( int i = maxStackNum; i > 0; i /= 2 )
				tempSize1++;
			tempSize1 *= numOfStacks;
			if( tempSize1 < answer ) 
				answer = tempSize1;
			if( numOfStacks < answer ) 
				numOfStacks = tempSize1;
		}
		plates.clear();
		cout << answer << endl;
	}*/
	return 0;
}

#include <iostream>
#include <string>
#include<conio.h>

using namespace std;

const string CASE = "Case #";
const string BAD = "Bad magician!";
const string CHEATED = "Volunteer cheated!";

const int BAD_ANSWER = -1;
const int CHEATED_ANSWER = -2;

// guess an answer for magic trick
int guess(int case_num)
{
	int first_answer;
	int second_answer;
	int first_arrange[16];
	int second_arrange[16];

	cin>>first_answer;
	for(int i=0;i<16;i++) 
    {
		cin>>first_arrange[i];
	}

	cin>>second_answer;
	for(int i=0;i<16;i++) 
    {
		cin>>second_arrange[i];
	}

	int found[4]={0};
	int num[4]={0};

	for(int i=0;i<4;i++)
     {
        int s=first_answer-1;
		int card_Num=first_arrange[4*s + i];
		for(int j=0;j<16;j++)
         {
			if(card_Num==second_arrange[j]) 
            {
				found[j/4]++;
				num[j/4]=card_Num;
			}
		}
	}

	if(found[second_answer-1]==0) 
    {
		return CHEATED_ANSWER;
	}
	if(found[second_answer-1]>1) 
    {
		return BAD_ANSWER;
	}
	return num[second_answer-1];
}

int main() 
{
	int T; // number of test cases
	cin>>T;
	for(int i=0;i<T;i++) 
    {
		int a=guess(i+1);
		switch(a) 
        {
			case BAD_ANSWER:
				cout<<CASE<<(i+1)<<": "<<BAD<<"\n";	
				break;
			case CHEATED_ANSWER:
				cout<<CASE<<(i+1)<<": "<<CHEATED<<"\n";	
				break;
			default:
				cout<<CASE<<(i+1)<<": "<<a<<"\n";	
				break;
		}
	}
	getch();
	return 0;
}

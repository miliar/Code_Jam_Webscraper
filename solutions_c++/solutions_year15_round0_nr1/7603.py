#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int how_many_not_shy_people_we_need(int*,int);
int main()
{
	ifstream op("A-large.in");
	ofstream out("out.txt");
	int max,temp,*iamtooshy,shypeoplecount,Need_Not_Shy;
	string number_of_shy_people;
	op >> max;
	for (int i = 0; i < max; i++){
		op >> shypeoplecount;
		iamtooshy = new int[shypeoplecount + 1];
			op >> number_of_shy_people;
			for (int j = 0; j <= shypeoplecount; j++){
				iamtooshy[j] = number_of_shy_people[j];
				iamtooshy[j] -= 48;
			}
		
		Need_Not_Shy = how_many_not_shy_people_we_need(iamtooshy, shypeoplecount + 1);
		delete[] iamtooshy;
		out << "Case #" << i + 1 << ": " <<Need_Not_Shy<< endl;
	}
	op.close();
	out.close();
	return 0;
}
int how_many_not_shy_people_we_need(int* shy,int number_of_shy_people){
	int shy_level = shy[0], need_people = 0;
	for (int i = 1; i < number_of_shy_people; i++){
		if (shy[i]>0)
			while ((shy_level+need_people) < i){
				need_people++;
			}
		shy_level += shy[i];
	}
	return need_people;
	
}
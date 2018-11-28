#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int flipPancake (int top,int bottom,string pancake);

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in.txt");
	fout.open("Bout.txt");
	int T,time;
	string array;
	fin >> T;
	for (int i=1;i<=T;i++)
	{
		array.empty();
		fin >> array;
		time = 0;
		time = flipPancake(1,array.length(),array);
		fout << "Case #" << i << ": " << time << endl;
	}
	fin.close();
	fout.close();
	return 0;
}

int flipPancake(int top,int bottom,string pancake)
{
	int B(bottom),count(1);
	if (bottom>top)
	{
		if (pancake[bottom-1]=='+') return flipPancake(top,bottom-1,pancake);
		else 
		{
			while (pancake[B-2]=='-' && B>=2){count++;B--;}
			if (count == bottom-top+1) return 1;
			else if (count > 1) return flipPancake(top,bottom-count,pancake)+2;
			else return flipPancake(top,bottom-1,pancake)+2;
		}
	}
	else
	{
		if (pancake[top-1]=='-') return 1;
		else return 0;
	}
}

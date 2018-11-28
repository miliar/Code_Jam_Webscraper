#include<iostream>
#include<fstream>
#include<string>
#include<stack>
using namespace std;
void flip(string &Pancakes)
{
	if (Pancakes[0] == '-')
	for (unsigned short i = 0; i<Pancakes.size(); i++)
	{
		{ Pancakes[i] = '+'; }
	}
	else
	for (unsigned short i = 0; i<Pancakes.size(); i++)
	{
		{ Pancakes[i] = '-'; }
	}
}
stack<string>get_stack(string &Pancakes)
{
	stack<string>x;
	for ( short i = Pancakes.size() - 1; i >= 0; i--)
	{
		x.push(Pancakes.substr(i, 1));
	}
	return x;
}
int proc(string &Pancakes)
{
	stack<string>x = get_stack(Pancakes);
	string y="";
	string z = x.top();y+=z;x.pop();
	int counter=0;
  while (true){
				while (!x.empty() && x.top() == z){ y += z; x.pop(); }
				if (x.empty()){ if (z == "+") return counter; else return counter + 1; }
				else
				{
				flip(y); counter++;
				for ( short i = y.size() - 1; i >= 0; i--)
					{
					x.push(y.substr(i, 1));
					}
				flip(z); y = "";
				}
			 }
}
int main()
{
	string l; unsigned short max,nu;
	fstream in, out;
	in.open("C:/Users/rou2a/Desktop/x.txt");
	out.open("C:/Users/rou2a/Desktop/y.txt");
	in >> l; max = stoi(l);
	for (unsigned short i = 1; i <= max; i++)
	{
		in >> l;
		nu = proc(l);
		out << "Case #" << i << ": " << nu << endl;
	}
	return 0;
}

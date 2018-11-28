#include<iostream>
#include<algorithm>
#include<fstream>
#include<deque>
#include<vector>
int main()
{
	std::ifstream in;
	in.open("D-large.in");
	std::ofstream out;
	out.open("D-large.out");
	int T, c=0, n, dw, w;
	double x;
	std::deque<double> a, b;
	std::vector<double> d, e;
	in>>T;
	while(T--)
	{
		c++;
		dw = w =0;
		a.clear();
		b.clear();
		d.clear();
		e.clear();
		in>>n;

		
		for(int i=0; i<n; i++)
		{
			in>>x;
			a.push_back(x);
			d.push_back(x);
		}

		for(int i=0; i<n; i++)
		{
			in>>x;
			b.push_back(x);
			e.push_back(x);
		}
		if(n == 1)
		{
			if(a.front() > b.front())
				out<<"Case #"<<c<<": 1 1\n";
			else
				out<<"Case #"<<c<<": 0 0\n";
			continue;
		}

		std::sort(a.begin(), a.end());
		std::sort(b.begin(), b.end());
		std::sort(d.begin(), d.end());
		std::sort(e.begin(), e.end());


		//for(std::vector<double>::iterator i=d.begin(), j = e.begin(); i != d.end(); i++, j++)
		while(!d.empty())
		{
			std::vector<double>::iterator i=d.begin();
			std::vector<double>::iterator up;
			up = std::upper_bound (e.begin(), e.end(), *i);
			if(up == e.end())
			{
				w++;
				d.erase(i);
				e.erase(e.begin());
			}
			else
			{
				d.erase(i);
				e.erase(up);
			}
		}

		while(!a.empty())
		{
			if((a.front() > b.front()))
			{
				dw++;
				a.pop_front();
				b.pop_front();
			}
			else
			{
				a.pop_front();
				b.pop_back();
			}
		}
      
		out<<"Case #"<<c<<": "<<dw<<" "<<w<<"\n";

	}
}
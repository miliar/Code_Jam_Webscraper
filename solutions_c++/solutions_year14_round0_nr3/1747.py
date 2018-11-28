#include <iostream>
#include <fstream>
#include <functional>

#include <boost/format.hpp>
#include <string>

std::string format_(boost::format &fmt)
{ return fmt.str(); }

template <typename A, typename ... Args>
std::string format_(boost::format &fmt, const A& a, Args...args)
{ return format_(fmt % a, args...); }

template <typename ... Args>
std::string format(const std::string &fmt, Args...args)
{
        boost::format fmt_(fmt);
        return format_(fmt_, args...);
}


typedef unsigned long field_t;

#define F(x,y) ((field & (1<<((x)+X*(y)))) != 0)
#define F_(x,y) ((x) < 0 || (x) >= X || (y) < 0 || (y) >= Y ? \
	0 : \
	(field & (1<<((x)+X*(y)))) != 0)

bool click(int X, int Y, int M, int cx, int cy, field_t field)
{
	field_t mark = 0;
	int res = 0;

	std::function<void(int,int)> c = [&](int x, int y)
	{
		if(x < 0 || x >= X || y < 0 || y >= Y)
			return;

		field_t mark_ = 1 << (x+X*y);

		if(mark & mark_ || field & mark_)
			return;

		res++;

		mark |= mark_;

		bool mines = F_(x-1,y-1) || F_(x,y-1) || F_(x+1,y-1)
		          || F_(x-1,y  ) ||     0     || F_(x+1,y  )
		          || F_(x-1,y+1) || F_(x,y+1) || F_(x+1,y+1);
		
		if(mines)
			return;

		c(x-1,y-1); c(x  ,y-1); c(x+1,y-1);
		c(x-1,y  );             c(x+1,y  );
		c(x-1,y+1); c(x  ,y+1); c(x+1,y+1);
	};

	c(cx, cy);

	return res == X*Y - M;	
}

void test(int X, int Y, int M)
{
	
	field_t field, cx, cy;
	if(X*Y-1 == M)
	{
		field = ~0u;
		cx = X-1;
		cy = Y-1;
		goto print;
	}

	for(field = 0; field < (1 << (X*Y)); field++)
	{

		int sum = 0;
		for(int y = 0; y < Y; y++) for(int x = 0; x < X; x++)
			sum += F(x,y);

		if(sum != M)
			continue;

		for(cy = 0; cy < Y; cy++) for(cx = 0; cx < X; cx++)
			if(F_(cx-1,cy-1) == 0 && F_(cx,cy-1) == 0 && F_(cx+1,cy-1) == 0
			&& F_(cx-1,cy  ) == 0 && F_(cx,cy  ) == 0 && F_(cx+1,cy  ) == 0
			&& F_(cx-1,cy+1) == 0 && F_(cx,cy+1) == 0 && F_(cx+1,cy+1) == 0)
					goto pok;
		continue;
	pok:
		if(!click(X,Y,M,cx,cy,field))
			continue;
		goto print;

	}

	//std::cout << "Impossible" << std::endl;
	return;

	print:

	std::ofstream f(format("out/%d_%d_%d.txt", X, Y, M));
	for(int y = 0; y < Y; y++)
	{
		for(int x = 0; x < X; x++)
			if(x == cx && y == cy)
				f << 'c';
			else
				f << (F(x,y)? '*' : '.');
		f << "\n";
	}
}

int main()
{
	for(int X = 1; X <= 5; X++)
		for(int Y = 1; Y <= 5; Y++)
			for(int M = 0; M < X*Y; M++)
				test(X,Y,M);
}

int main_()
{
	int count;
	std::cin >> count;
	for(int i = 1; i <= count; i++)
	{
		int X,Y,M;
		std::cin >> Y >> X >> M;
		std::cout << "Case #" << i << ":\n";
		test(X,Y,M);
	}
}

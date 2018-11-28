#include "stdafx.h"

template<>
void Prepare<ProblemA>()
{
}

Int R, C;
vector<string> grid;

struct XY
{
	enum Dir
	{
		N,
		U,
		L,
		R,
		D
	};
	Int x, y;
	bool operator==(XY xy)
	{
		return x == xy.x && y == xy.y;
	}
};
XY::Dir At(XY xy)
{
	switch (grid[xy.y][xy.x])
	{
	case '.':return XY::N;
	case '^':return XY::U;
	case '<':return XY::L;
	case '>':return XY::R;
	case 'v':return XY::D;
	default:
		return XY::N;
	}
}
void Set(XY xy, XY::Dir d)
{
	switch (d)
	{
	case XY::N:
		grid[xy.y][xy.x] = '.';
		break;
	case XY::U:
		grid[xy.y][xy.x] = '^';
		break;
	case XY::L:
		grid[xy.y][xy.x] = '<';
		break;
	case XY::D:
		grid[xy.y][xy.x] = 'v';
		break;
	case XY::R:
		grid[xy.y][xy.x] = '>';
		break;
	default:
		break;
	}
}
bool IsOut(XY xy)
{
	if (xy.x < 0) return true;
	if (xy.y < 0) return true;
	if (xy.x >= C) return true;
	if (xy.y >= R) return true;
}
struct Loc
{
	XY xy;
	XY::Dir d;

	bool operator==(Loc loc)
	{
		return xy == loc.xy && d == loc.d;
	}
};
Loc Back(Loc loc)
{
	switch (loc.d)
	{
	case XY::N:
		return loc;
		break;
	case XY::U:
	{
				  XY res = { loc.xy.x, loc.xy.y + 1 };
				  Loc locn = { res, loc.d };
				  return locn;
	}
		break;
	case XY::L:
	{
				  XY res = { loc.xy.x + 1, loc.xy.y };
				  Loc locn = { res, loc.d };
				  return locn;
	}
		break;
	case XY::D:
	{
				  XY res = { loc.xy.x, loc.xy.y - 1 };
				  Loc locn = { res, loc.d };
				  return locn;
	}
		break;
	case XY::R:
	{
				  XY res = { loc.xy.x - 1, loc.xy.y };
				  Loc locn = { res, loc.d };
				  return locn;
	}
		break;
	default:
		break;
	}

}
Loc Move(Loc loc)
{
	if (IsOut(loc.xy))
		return loc;
	if (At(loc.xy) != loc.d && At(loc.xy) != XY::N)
	{
		Loc locn = { loc.xy, At(loc.xy) };
		return Move(locn);
	}

	switch (loc.d)
	{
	case XY::N:
		return loc;
		break;
	case XY::U:
	{
				  XY res = { loc.xy.x, loc.xy.y - 1 };
				  Loc locn = { res, loc.d };
				  return locn;
	}
		break;
	case XY::L:
	{
				  XY res = { loc.xy.x - 1, loc.xy.y };
				  Loc locn = { res, loc.d };
				  return locn;
	}
		break;
	case XY::D:
	{
				  XY res = { loc.xy.x, loc.xy.y + 1 };
				  Loc locn = { res, loc.d };
				  return locn;
	}
		break;
	case XY::R:
	{
				  XY res = { loc.xy.x + 1, loc.xy.y };
				  Loc locn = { res, loc.d };
				  return locn;
	}
		break;
	default:
		break;
	}
}
Loc Walk(Loc loc1, Loc loc2)
{
	if (loc1.xy == loc2.xy)
		return loc2;
	if (IsOut(loc2.xy))
		return loc2;

	Loc loc1n = Move(loc1);
	Loc loc2n = Move(Move(loc2));

	return Walk(loc1n, loc2n);
}
Loc Walk(XY xy)
{
	Loc loc1 = { xy, XY::N };
	Loc loc2 = Move(loc1);
	return Walk(loc1, loc2);
}
bool Last(Loc loc)
{
	do
	{
		loc = Back(loc);
	} while (At(loc.xy) == XY::N);
	if (IsOut(loc.xy))
		return false;
	XY::Dir d = At(loc.xy);
	for (Int i = 1; i < 5; i++)
	{
		Loc loct = loc;
		loct.d = (XY::Dir)i;

		do
		{
			loct = Back(loct);
		} while (!IsOut(loct.xy) && At(loct.xy) == XY::N);
		if (!IsOut(loct.xy))
		{
			Set(loc.xy, (XY::Dir)(5-i));
			return true;
		}
	}
	return false;
}

template<> 
void Solve<ProblemA>(Int T)
{
	R = ReadNum();
	C = ReadNum();
	grid.clear();
	for (Int r = 0; r < R; r++)
	{
		grid.push_back(ReadStr());
	}
	Int res = 0;
	for (Int x = 0; x < C; x++)
	{
		for (Int y = 0; y < R; y++)
		{
			XY xy = { x, y };
			if (At(xy) == XY::N) continue;
			Loc loc = Walk(xy);
			if (IsOut(loc.xy))
			{
				if (Last(loc))
				{
					res++;
				}
				else
				{
					Write(T, "IMPOSSIBLE");
					return;
				}
			}
		}
	}
	Write(T, res);
}
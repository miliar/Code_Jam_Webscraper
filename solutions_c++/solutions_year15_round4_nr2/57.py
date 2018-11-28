#ifndef KOMAKI_LOCAL
#define NDEBUG
#endif

#include <bits/stdc++.h>
#include <sys/time.h>
#include <unistd.h>
using namespace std;
#define i64         int64_t
#define rep(i, n)   for(i64 i = 0; i < ((i64)(n)); ++i)
#define sz(v)       ((i64)((v).size()))
#define bit(n)      (((i64)1)<<((i64)(n)))
#define all(v)      (v).begin(), (v).end()

std::string dbgDelim(int &i){ return (i++ == 0 ? "" : ", "); }
#define dbgEmbrace(exp) { int i = 0; os << "{"; { exp; } os << "}"; return os; }
template <class T> std::ostream& operator<<(std::ostream &os, std::vector<T> v);
template <class T> std::ostream& operator<<(std::ostream &os, std::set<T> v);
template <class T> std::ostream& operator<<(std::ostream &os, std::queue<T> q);
template <class T> std::ostream& operator<<(std::ostream &os, std::priority_queue<T> q);
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::pair<T, K> p);
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::map<T, K> mp);
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::unordered_map<T, K> mp);
template <int INDEX, class TUPLE> void dbgDeploy(std::ostream &os, TUPLE tuple){}
template <int INDEX, class TUPLE, class H, class ...Ts> void dbgDeploy(std::ostream &os, TUPLE t)
{ os << (INDEX == 0 ? "" : ", ") << get<INDEX>(t); dbgDeploy<INDEX + 1, TUPLE, Ts...>(os, t); }
template <class T, class K> void dbgDeploy(std::ostream &os, std::pair<T, K> p, std::string delim)
{ os << "(" << p.first << delim << p.second << ")"; }
template <class ...Ts> std::ostream& operator<<(std::ostream &os, std::tuple<Ts...> t)
{ os << "("; dbgDeploy<0, std::tuple<Ts...>, Ts...>(os, t); os << ")"; return os; }
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::pair<T, K> p)
{ dbgDeploy(os, p, ", "); return os; }
template <class T> std::ostream& operator<<(std::ostream &os, std::vector<T> v)
{ dbgEmbrace( for(T t: v){ os << dbgDelim(i) << t; }); }
template <class T> std::ostream& operator<<(std::ostream &os, std::set<T> s)
{ dbgEmbrace( for(T t: s){ os << dbgDelim(i) << t; }); }
template <class T> std::ostream& operator<<(std::ostream &os, std::queue<T> q)
{ dbgEmbrace( for(; q.size(); q.pop()){ os << dbgDelim(i) << q.front(); }); }
template <class T> std::ostream& operator<<(std::ostream &os, std::priority_queue<T> q)
{ dbgEmbrace( for(; q.size(); q.pop()){ os << dbgDelim(i) << q.top();   }); }
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::map<T, K> mp)
{ dbgEmbrace( for(auto p: mp){ os << dbgDelim(i); dbgDeploy(os, p, "->"); }); }
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::unordered_map<T, K> mp)
{ dbgEmbrace( for(auto p: mp){ os << dbgDelim(i); dbgDeploy(os, p, "->"); }); }
#define DBG_OUT std::cerr
#define DBG_OVERLOAD(_1, _2, _3, _4, _5, _6, macro_name, ...) macro_name
#define DBG_LINE() { char s[99]; sprintf(s, "line:%3d | ", __LINE__); DBG_OUT << s; }
#define DBG_OUTPUT(v) { DBG_OUT << (#v) << "=" << (v); }
#define DBG1(v, ...) { DBG_OUTPUT(v); }
#define DBG2(v, ...) { DBG_OUTPUT(v); DBG_OUT << ", "; DBG1(__VA_ARGS__); }
#define DBG3(v, ...) { DBG_OUTPUT(v); DBG_OUT << ", "; DBG2(__VA_ARGS__); }
#define DBG4(v, ...) { DBG_OUTPUT(v); DBG_OUT << ", "; DBG3(__VA_ARGS__); }
#define DBG5(v, ...) { DBG_OUTPUT(v); DBG_OUT << ", "; DBG4(__VA_ARGS__); }
#define DBG6(v, ...) { DBG_OUTPUT(v); DBG_OUT << ", "; DBG5(__VA_ARGS__); }

#define DEBUG0() { DBG_LINE(); DBG_OUT << std::endl; }
#define DEBUG(...)                                                      \
  {                                                                     \
    DBG_LINE();                                                         \
    DBG_OVERLOAD(__VA_ARGS__, DBG6, DBG5, DBG4, DBG3, DBG2, DBG1)(__VA_ARGS__); \
    DBG_OUT << std::endl;                                               \
  }

/********************************************************************/
/**                                                                **/
/** Rule.1: Use g_double.                                          **/
/** Rule.2: You may use 'using namespace Geometry2D'               **/
/** Rule.3: You may change g_double to 'double' for acceleration.  **/
/** Rule.4: Take care about "EPS" (= 1e-12).                       **/
/**         EPS * max(1.0, 1e-6 * max(abs(gd0), abs(gd1)));        **/
/**                                                                **/
/**                                                                **/
/********************************************************************/

typedef long double g_double; // Changing this needs an EPS change.
namespace Geometry2D
{
  static const g_double PI = (g_double)3.14159265358979323846264338327950288l;
  static const g_double EPS = 1e-11;
  class Vector;

  class Point
  {
  public:
    g_double x, y;
    Point(g_double x, g_double y);
    Point(Vector v);
    Point(){};
  };
  
  class Vector
  {
  public:
    Point initial_point;
    Point terminate_point;
    Vector(Point initial_point, Point terminate_point);
    Vector(){};
  };
  
  class Polygon
  {
  public:
    std::vector<Point> points;
    
    int size();

    void add(Point p);

    Point& operator[](int index);
  };
  
  class Circle
  {
  public:
    Point center;
    g_double radius;
    
    Circle(Point center, g_double radius);
    Circle(){}
  };
  
  static int ccw(Point p0, Point p1);                 // 0: forward, 1: clockwise, 2: back, 3: counter-clockwise.
  static int ccw(Vector v0, Vector v1);               // 0: forward, 1: clockwise, 2: back, 3: counter-clockwise.
  static g_double getAngle360(Vector v0, Vector v1);  // Caution: this is volunearable due to significant digits!! Returns the clockwise-angle from v0 to v1.
  static g_double crossProduct(Point p0, Point p1);   // Caution: Use ccw!! This breaks significant digits!! p0.x * p1.y - p1.x * p0.y.
  static g_double crossProduct(Vector v0, Vector v1); // Caution: Use ccw!! This breaks significant digits!! Calculate the cross product of two vectors.
  static bool isOrthogonal(Vector v0, Vector v1);     // Returns whether two vectors are orthogonal or not.
  
  static Point add(Point p0, Point p1);  // Point(p0.x + p1.x, p0.y + p1.y).
  static Point sub(Point p0, Point p1);  // Point(p0.x - p1.x, p0.y - p1.y).
  static Point mul(Point p, g_double d); // Point(p0.x - p1.x, p0.y - p1.y).
  
  static bool isPointOnLine(Point p, Vector v);    // Checks whether a point is on an infinite line.
  static bool isPointOnSegment(Point p, Vector v); // Checks whether a point is on a finite segment.
  
  static Point getPointOnLineX(Vector v, g_double x);        // Returns a point on an infinite line with 'x' as x-cordinate.
  static Point getPointOnLineY(Vector v, g_double y);        // Returns a point on an infinite line with 'y' as y-cordinate.
  static Point getNearestPointOnLine(Vector v, Point p);     // Returns a point on an infinite line which is nearest to a point.
  static Point getNearestPointOnSegment(Vector v, Point p);  // Returns a point on an infinite line which is nearest to a point.
  static Point getIntersectionOfLines(Vector v0, Vector v1); // Caution: No check on parallel lines!! Use isParallel. Returns the intersection of two infinite lines.
  
  static bool isEqual(g_double gd0, g_double gd1); // Caution: Never do isEqual(d0 - i1, 0). Take care about significant digits!!
  static bool isEqual(Point p0, Point p1);         // Caution: Never do isEqual(v0 - v1, 0). Take care about significant digits!!
  static bool isEqual(Vector v0, Vector v1);       // Checks whether initial and terminate points matche or not.
  static bool isEqual(Circle c0, Circle c1);       // Checks whether initial and terminate points matche or not.
  static bool isLess(g_double gd0, g_double gd1);  // Take care about EPS.
  static bool isLess(Point p0, Point p1);          // Returns (p0.x < p1.x) || (p0.x == p1.x && p0.y < p1.y)
  
  static bool hasIntersection(Vector v0, Vector v1);   // Checks whether two lines intersect or not.
  
  static g_double getDistance(Point p0, Point p1);   // Returns the distance of two points.
  static g_double getDistance(Vector v, Point p);    // Returns the distance of two segments.
  static g_double getDistance(Vector v0, Vector v1); // Returns the distance of two segments.
  static g_double getLength(Vector v);               // Returns the length of a finite line.
  
  static g_double getArea(Polygon polygon);                     // Returns the area of a polygon.
  static g_double getArea(Circle circle);                       // Returns the area of a circle.
  static Polygon getConvexHull(Polygon polygon);                // Returns a convex hull out of a polygon.
  static int isPointInPolygon(Point point, Polygon &polgyon);        // 0: ouside, 1: on a line, 2: inside and no touch.
  static int isPointInConvexHull(Point point, Polygon &convex_hull); // 0: ouside, 1: on a line, 2: inside and no touch.
  static int isPointInCircle(Point point, Circle circle);            // 0: ouside, 1: on a line, 2: inside and no touch.
  
  static vector<Point> getIntersections(Circle c0, Circle c1);                        // Retruns intersections of two circles.
  static vector<Point> getTangents(Circle circle, Point point);                       // Returns tangents of a circle through a point.
  static vector<tuple<Point, Point>> getInternalCommonTangents(Circle c0, Circle c1); // Returns internal common tangents of two circles.
  static vector<tuple<Point, Point>> getExternalCommonTangents(Circle c0, Circle c1); // Returns external common tangents of two circles.
};

inline bool Geometry2D::isEqual(Circle c0, Circle c1)
{
  if(!isEqual(c0.center, c1.center)) return false;
  if(!isEqual(c0.radius, c1.radius)) return false;
  return true;
}

inline Geometry2D::Point Geometry2D::mul(Point p, g_double d)
{
  return Point(p.x * d, p.y * d);
}

inline Geometry2D::Point::Point(Vector v)
{
  this->x = v.terminate_point.x - v.initial_point.x;
  this->y = v.terminate_point.y - v.initial_point.y;
}

inline vector<tuple<Geometry2D::Point, Geometry2D::Point>> Geometry2D::getExternalCommonTangents(Circle c0, Circle c1)
{
  if(isEqual(c0, c1)) return vector<tuple<Point, Point>>();
  if(isEqual(c0.radius, c1.radius)){
    vector<tuple<Point, Point>> tangents;
    Point orthogonal = Point((c1.center.y - c0.center.y), -(c1.center.x - c0.center.x));
    rep(up_down, 2){
      tangents.push_back(make_tuple(
          add(c0.center, mul(mul(orthogonal, up_down ? 1 : -1), c0.radius / getLength(Vector(Point(0, 0), orthogonal)))),
          add(c1.center, mul(mul(orthogonal, up_down ? 1 : -1), c1.radius / getLength(Vector(Point(0, 0), orthogonal))))));
    }
    return tangents;     
  }
  g_double x = (c0.center.x * c1.radius - c1.center.x * c0.radius) / (c1.radius - c0.radius);
  g_double y = (c0.center.y * c1.radius - c1.center.y * c0.radius) / (c1.radius - c0.radius);
  Point middle(x, y);
  if(isPointInCircle(middle, c0) == 2) return vector<tuple<Point, Point>>();
  if(isPointInCircle(middle, c0) == 1) return vector<tuple<Point, Point>>({make_tuple(middle, middle)});
  vector<Point> tangents0 = getTangents(c0, middle);
  vector<Point> tangents1 = getTangents(c1, middle);
  if(tangents0.size() != 2) cerr << "error in line." << __LINE__ << endl;
  if(tangents1.size() != 2) cerr << "error in line." << __LINE__ << endl;
  if(!isPointOnLine(middle, Vector(tangents0[0], tangents1[0]))) swap(tangents0[0], tangents0[1]);
  return vector<tuple<Point, Point>>({
      make_tuple(tangents0[0], tangents1[0]),
      make_tuple(tangents0[1], tangents1[1])});
}

inline vector<tuple<Geometry2D::Point, Geometry2D::Point>> Geometry2D::getInternalCommonTangents(Circle c0, Circle c1)
{
  g_double x = (c0.center.x * c1.radius + c1.center.x * c0.radius) / (c0.radius + c1.radius);
  g_double y = (c0.center.y * c1.radius + c1.center.y * c0.radius) / (c0.radius + c1.radius);
  Point middle(x, y);
  if(isPointInCircle(middle, c0) == 2) return vector<tuple<Point, Point>>();
  if(isPointInCircle(middle, c0) == 1) return vector<tuple<Point, Point>>({make_tuple(middle, middle)});
  vector<Point> tangents0 = getTangents(c0, middle);
  vector<Point> tangents1 = getTangents(c1, middle);
  if(tangents0.size() != 2) cerr << "error in line." << __LINE__ << endl;
  if(tangents1.size() != 2) cerr << "error in line." << __LINE__ << endl;
  if(!isPointOnLine(middle, Vector(tangents0[0], tangents1[0]))) swap(tangents0[0], tangents0[1]);
  return vector<tuple<Point, Point>>({
      make_tuple(tangents0[0], tangents1[0]),
      make_tuple(tangents0[1], tangents1[1])});
}

inline vector<Geometry2D::Point> Geometry2D::getTangents(Circle circle, Point point)
{
  g_double dx = point.x - circle.center.x;
  g_double dy = point.y - circle.center.y;
  g_double d = dx * dx + dy * dy;
  g_double e = d - circle.radius * circle.radius;
  if(e < 0) return vector<Point>();
  e = sqrt(e);
  g_double f = circle.radius / d;
  g_double dx_cr = dx * circle.radius;
  g_double dy_cr = dy * circle.radius;
  g_double dx_e = dx * e;
  g_double dy_e = dy * e;
  vector<Point> tangents;
  tangents.push_back(add(circle.center, Point((dx_cr + dy_e) * f, (dy_cr - dx_e) * f)));
  tangents.push_back(add(circle.center, Point((dx_cr - dy_e) * f, (dy_cr + dx_e) * f)));
  return tangents;
}

inline vector<Geometry2D::Point> Geometry2D::getIntersections(Circle c0, Circle c1)
{
  if(isEqual(c0.center, c1.center)) return vector<Point>();
  g_double dx = c0.center.x - c1.center.x;
  g_double dy = c0.center.y - c1.center.y;
  g_double base = dx * dx + dy * dy;
  g_double a = (base + c1.radius * c1.radius - c0.radius * c0.radius) * 0.5;
  g_double b = base * c1.radius * c1.radius - a * a;
  if(isLess(b, 0)) return vector<Point>();
  b = sqrt(b);
  vector<Point> intersections;
  intersections.push_back(add(c1.center, mul(Point(a * dx + dy * b, a * dy - dx * b), 1.0 / base)));
  intersections.push_back(add(c1.center, mul(Point(a * dx - dy * b, a * dy + dx * b), 1.0 / base)));
  return intersections;
}

inline int Geometry2D::isPointInCircle(Point point, Circle circle)
{
  g_double dist = getDistance(circle.center, point);
  if(isLess(dist, circle.radius)) return 2;
  if(isEqual(dist, circle.radius)) return 1;
  return 0;
}

inline g_double Geometry2D::getArea(Circle circle)
{
  return PI * circle.radius * circle.radius;
}

inline Geometry2D::Circle::Circle(Point center, g_double radius)
{
  this->center = center;
  this->radius = radius;
}

inline g_double Geometry2D::getDistance(Vector v0, Vector v1)
{
  if(hasIntersection(v0, v1)) return 0.0;
  g_double distance = getDistance(v0, v1.initial_point);
  distance = std::min(distance, getDistance(v0, v1.terminate_point));
  distance = std::min(distance, getDistance(v1, v0.initial_point));
  distance = std::min(distance, getDistance(v1, v0.terminate_point));
  return distance;
}

inline g_double Geometry2D::getDistance(Vector v, Point p)
{
  Point nearest = getNearestPointOnLine(v, p);
  if(isPointOnSegment(nearest, v)) return getDistance(nearest, p);
  return std::min(getDistance(v.initial_point, p), getDistance(v.terminate_point, p));
}

inline bool Geometry2D::hasIntersection(Vector v0, Vector v1)
{
  Point p = getIntersectionOfLines(v0, v1);
  if(!isPointOnSegment(p, v0)) return false;
  if(!isPointOnSegment(p, v1)) return false;
  return true;
}

inline g_double Geometry2D::crossProduct(Point p0, Point p1)
{
  return p0.x * p1.y - p1.x * p0.y;
}

inline g_double Geometry2D::crossProduct(Vector v0, Vector v1)
{
  return crossProduct(Point(v0), Point(v1));
}

inline int Geometry2D::ccw(Point p0, Point p1)
{
  if(isEqual(p0.x * p1.y, p0.y * p1.x)){
    if(isLess(p0.x * p1.x, 0)) return 2; // backward.
    if(isLess(p0.y * p1.y, 0)) return 2; // backward.
    return 0; // forward.
  }
  if(isLess(p0.x * p1.y, p0.y * p1.x)) return 1; // clockwise.
  return 3; // counter-clockwise.
}

inline int Geometry2D::ccw(Vector v0, Vector v1)
{
  return ccw(Point(v0), Point(v1));
}

inline g_double Geometry2D::getAngle360(Vector v0, Vector v1)
{
  g_double angle0 = atan2l(v0.terminate_point.y - v0.initial_point.y, v0.terminate_point.x - v0.initial_point.x);
  g_double angle1 = atan2l(v1.terminate_point.y - v1.initial_point.y, v1.terminate_point.x - v1.initial_point.x);
  g_double angle = (angle1 - angle0) / (2.0 * PI) * 360.0;
  while(isLess(angle, 0)) angle += 360.0;
  while(isLess(360, angle) || isEqual(360, angle)) angle -= 360;
  return angle;
}

inline bool Geometry2D::isOrthogonal(Vector v0, Vector v1)
{
  Point p = sub(v1.terminate_point, v1.initial_point);
  Point orthogonal(p.y, -p.x);
  return (ccw(sub(v0.terminate_point, v0.initial_point), orthogonal) & 1) == 0;
}

inline int Geometry2D::Polygon::size()
{
  return (int)points.size();
}

inline Geometry2D::Point& Geometry2D::Polygon::operator [](int index)
{
  return points[index];
}

inline void Geometry2D::Polygon::add(Point p)
{
  points.push_back(p);
}

inline bool Geometry2D::isLess(g_double gd0, g_double gd1)
{
  return gd0 < gd1 && !isEqual(gd0, gd1);
}

inline bool Geometry2D::isLess(Point p0, Point p1)
{
  if(isEqual(p0.x, p1.x)) return isLess(p0.y, p1.y);
  return isLess(p0.x, p1.x);
}


inline bool Geometry2D::isPointOnLine(Point p, Vector v)
{
  if(isEqual(v.initial_point, p)) return true;
  if(isEqual(v.terminate_point, p)) return true;
  return (ccw(v, Vector(v.initial_point, p)) & 1) == 0;
}

inline bool Geometry2D::isPointOnSegment(Point p, Vector v)
{
  if(isLess(p.x, min(v.initial_point.x, v.terminate_point.x))) return false;
  if(isLess(p.y, min(v.initial_point.y, v.terminate_point.y))) return false;
  if(isLess(max(v.initial_point.x, v.terminate_point.x), p.x)) return false;
  if(isLess(max(v.initial_point.y, v.terminate_point.y), p.y)) return false;
  return isPointOnLine(p, v);
}

inline Geometry2D::Point Geometry2D::getIntersectionOfLines(Vector v0, Vector v1)
{
  g_double dx0 = v0.terminate_point.x - v0.initial_point.x;
  g_double dy0 = v0.terminate_point.y - v0.initial_point.y;
  g_double dx1 = v1.terminate_point.x - v1.initial_point.x;
  g_double dy1 = v1.terminate_point.y - v1.initial_point.y;
  if(isEqual(dx0 * dy1, dx1 * dy0)){
    if(isPointOnSegment(v0.initial_point, v1)) return v0.initial_point;
    if(isPointOnSegment(v1.initial_point, v0)) return v1.initial_point;
    if(isPointOnSegment(v0.terminate_point, v1)) return v0.terminate_point;
    if(isPointOnSegment(v1.terminate_point, v0)) return v1.terminate_point;
    return Point(-1e100, -1e100);
  }
  g_double den = dx1 * dy0 - dy1 * dx0;
  g_double d =
      ((v0.initial_point.x - v1.initial_point.x) * dy0 - 
       (v0.initial_point.y - v1.initial_point.y) * dx0) / den;
  return Point(v1.initial_point.x + dx1 * d, v1.initial_point.y + dy1 * d);
}


inline Geometry2D::Point Geometry2D::getNearestPointOnSegment(Vector v, Point p)
{
  g_double dx = v.terminate_point.x - v.initial_point.x;
  g_double dy = v.terminate_point.y - v.initial_point.y;
  Point nearest = getIntersectionOfLines(v, Vector(p, add(p, Point(dy, -dx))));
  if(isPointOnSegment(nearest, v)) return nearest;
  if(getDistance(v.initial_point, p) < getDistance(v.terminate_point, p)) return v.initial_point;
  return v.terminate_point;
}

inline Geometry2D::Point Geometry2D::getNearestPointOnLine(Vector v, Point p)
{
  g_double dx = v.terminate_point.x - v.initial_point.x;
  g_double dy = v.terminate_point.y - v.initial_point.y;
  return getIntersectionOfLines(v, Vector(p, add(p, Point(dy, -dx))));
}

inline Geometry2D::Point Geometry2D::getPointOnLineX(Vector v, g_double x)
{
  if(isEqual(v.initial_point.y, v.terminate_point.y)) return Point(x, v.initial_point.y);
  g_double dx = v.initial_point.x - v.terminate_point.x;
  g_double dy = v.initial_point.y - v.terminate_point.y;
  return Point(x, v.initial_point.y + (x - v.initial_point.x) * dy / dx);
}

inline Geometry2D::Point Geometry2D::getPointOnLineY(Vector v, g_double y)
{
  if(isEqual(v.initial_point.x, v.terminate_point.x)) return Point(v.initial_point.x, y);
  g_double dx = v.initial_point.x - v.terminate_point.x;
  g_double dy = v.initial_point.y - v.terminate_point.y;
  return Point(v.initial_point.x + (y - v.initial_point.y) * dx / dy, y);
}


inline g_double Geometry2D::getDistance(Point p0, Point p1)
{
  g_double dx = p0.x - p1.x;
  g_double dy = p0.y - p1.y;
  return sqrt(dx * dx + dy * dy);
}

inline g_double Geometry2D::getLength(Vector v)
{
  return getDistance(v.initial_point, v.terminate_point);
}

inline Geometry2D::Point Geometry2D::add(Point p0, Point p1)
{
  return Point(p0.x + p1.x, p0.y + p1.y);
}

inline Geometry2D::Point Geometry2D::sub(Point p0, Point p1)
{
  return Point(p0.x - p1.x, p0.y - p1.y);
}


inline Geometry2D::Point::Point(g_double x, g_double y)
{
  this->x = x;
  this->y = y;
}

inline Geometry2D::Vector::Vector(Point initial_point, Point terminate_point)
{
  this->initial_point = initial_point;
  this->terminate_point = terminate_point;
}

inline bool Geometry2D::isEqual(g_double gd0, g_double gd1)
{
  return abs(gd0 - gd1) <= EPS * std::max((g_double)1.0, 1e-6 * std::max(abs(gd0), abs(gd1)));
}

inline bool Geometry2D::isEqual(Point p0, Point p1)
{
  if(!isEqual(p0.x, p1.x)) return false;
  if(!isEqual(p0.y, p1.y)) return false;
  return true;
}

inline bool Geometry2D::isEqual(Vector v0, Vector v1)
{
  if(!isEqual(v0.initial_point, v1.initial_point)) return false;
  if(!isEqual(v0.terminate_point, v1.terminate_point)) return false;
  return true;
}

inline Geometry2D::Polygon Geometry2D::getConvexHull(Polygon polygon)
{
  if(polygon.size() <= 2) return polygon;
  sort(polygon.points.begin(), polygon.points.end(), [](Point p0, Point p1){ return isLess(p0, p1); });
  
  Polygon convex_hull;
  convex_hull.points = std::vector<Point>(polygon.size() * 2);
  
  int k = 0;
  for(int i = 0; i < polygon.points.size(); convex_hull.points[k++] = polygon.points[i++]){
    while(true){
      if(k < 2) break;
      if(ccw(sub(convex_hull.points[k - 1], convex_hull.points[k - 2]), 
          sub(polygon.points[i], convex_hull.points[k - 2])) == 1) break;
      --k;
    }
  }
  for(int i = (int)polygon.points.size() - 2, t = k + 1; 0 <= i; convex_hull.points[k++] = polygon.points[i--]){
    while(true){
      if(k < t) break;
      if(ccw(sub(convex_hull.points[k - 1], convex_hull.points[k - 2]), 
          sub(polygon.points[i], convex_hull.points[k - 2])) == 1) break;
      --k;
    }
  }
  convex_hull.points.resize(k - 1);
  
  return convex_hull;
}

inline int Geometry2D::isPointInPolygon(Point point, Polygon &polygon)
{
  bool is_in = false;
  for(int i = 0; i < polygon.size(); ++i){
    Point p0 = polygon[i];
    Point p1 = polygon[(i + 1) % polygon.size()];
    if(p0.y < p1.y) swap(p0, p1);
    Vector v0(p0, p1);
    Vector v1(p0, point);
    if((ccw(v0, v1) & 1) == 0 && isPointOnSegment(point, v0)) return 1;
    if(!isLess(point.y, p0.y)) continue;
    if(isLess(point.y, p1.y) && !isEqual(point.y, p1.y)) continue;
    if(ccw(v0, v1) == 1) is_in = !is_in;
  }
  return is_in ? 2 : 0;
}

inline int Geometry2D::isPointInConvexHull(Point point, Polygon &convex_hull)
{
  convex_hull.points.push_back(convex_hull[0]);
  
  int middle = -1;
  {
    int low = 0, high = convex_hull.size();
    while(low + 1 < high){
      int mid0 = (low * 2 + high) / 3;
      int mid1 = (low + 2 * high) / 3;
      if(isLess(convex_hull[mid0], convex_hull[mid1])) low = mid0 + 1;
      else high = mid1;
    }
    middle = low;
  }

  if(isLess(point.x, convex_hull[0].x)){ convex_hull.points.pop_back(); return false; }
  if(isLess(convex_hull[middle].x, point.x)){ convex_hull.points.pop_back(); return false; }

  {
    int left = 0, right = middle;
    while(left + 1 < right){
      int mid = (left + right) >> 1;
      if(isLess(point, convex_hull[mid])) right = mid;
      else left = mid;
    }

    Vector v(convex_hull[left], convex_hull[left + 1]);
    if(isPointOnSegment(point, v)){
      convex_hull.points.pop_back();
      return 1;
    }
    if(!isLess(point, getPointOnLineX(v, point.x))){
      convex_hull.points.pop_back();
      return 0;
    }
  }

  {
    int left = (int)convex_hull.size() - 1, right = middle;
    while(right + 1 < left){
      int mid = (left + right) >> 1;
      if(isLess(point, convex_hull[mid]) || isEqual(point, convex_hull[middle])) right = mid;
      else left = mid;
    }

    Vector v(convex_hull[right], convex_hull[right + 1]);
    if(isPointOnSegment(point, v)){
      convex_hull.points.pop_back();
      return 1;
    }
    if(isLess(point, getPointOnLineX(v, point.x))){
      convex_hull.points.pop_back();
      return 0;
    }
  }
  convex_hull.points.pop_back();
  return 2;
}

inline g_double Geometry2D::getArea(Polygon polygon)
{
  g_double area = 0;
  for(int i = 0; i < polygon.size(); ++i){
    area += crossProduct(polygon[i], polygon[(i + 1) % polygon.size()]);
  }
  return abs(area) * 0.5;
}

using namespace Geometry2D;

bool check(g_double volume, vector<g_double> volumes,
           g_double temperature, vector<g_double> temperatures,
           double duration, i64 n)
{
  double eps = 1e-10;
  double geta = 100000;
  Polygon convex_hull;
  convex_hull.add(Point(volume + geta, volume * temperature + geta));
  bool debug = false;//true;//false;//true;//false;
  rep(i, n){
    Polygon polygon;
    rep(j, sz(convex_hull)){
      polygon.add(convex_hull[j]);
      polygon.add(add(convex_hull[j], Point(-duration * volumes[i], -duration * volumes[i] * temperatures[i])));
    }
    convex_hull = getConvexHull(polygon);
    if(debug){
      DEBUG(sz(convex_hull));
      rep(j, sz(convex_hull)) DEBUG(convex_hull[j].x, convex_hull[j].y);
    }
  }
  if(debug){
    DEBUG(isPointInPolygon(Point(geta, geta), convex_hull));
    string line;
    cin >> line;
  }
  return isPointInPolygon(Point(geta, geta), convex_hull) != 0;
}


int main()
{
  i64 T;
  cin >> T;
  rep(test_case, T){
    g_double volume, temperature;
    i64 n;
    cin >> n >> volume >> temperature;
    vector<g_double> volumes(n), temperatures(n);
    rep(i, n) cin >> volumes[i] >> temperatures[i];
    /*
      DEBUG(volume, temperature);
      DEBUG(volumes);
      DEBUG(temperatures);
    */
    for(auto &v: volumes) v /= volume;
    volume = 1;
    if(*max_element(all(temperatures)) == temperature ||
       *min_element(all(temperatures)) == temperature){
      g_double total_volume = 0.0;
      rep(i, n)if(temperatures[i] == temperature) total_volume += volumes[i];
      printf("Case #%d: %0.10lf\n", (int)test_case + 1, (double)(volume / total_volume));
      continue;
    }
    if(*max_element(all(temperatures)) < temperature ||
       *min_element(all(temperatures)) > temperature){
      printf("Case #%d: IMPOSSIBLE\n", (int)test_case + 1);
      continue;
    }
    
    g_double low = 0, high = 1e20; 
    rep(loop, 200){
      double mid = (low + high) / 2;
      if(check(volume, volumes, temperature, temperatures, mid, n)){
        high = mid;
      }else{
        low = mid;
      }
    }
    printf("Case #%d: %0.20lf\n", (int)test_case + 1, (double)high);
  }
}




#ifndef COOKIE_H
#define COOKIE_H

#include <QDebug>
#include <QFile>
#include "QStringList"

class Cookie
{
public:
    Cookie();
    void start();
    double solve(double farmCost, double extraCookies, double totalCookiesNeeded );

};

#endif // COOKIE_H
